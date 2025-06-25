"""fastapi middleaware and exception handling concepts learning."""

import logging
from datetime import datetime
from datetime import timezone
import time
import traceback
import sys

# required to implement fastapi middleware
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.routing import Match
from starlette.responses import PlainTextResponse


from utils import ns2ms

# start loggers
customer_metrics_to_log = logging.getLogger("customer.metrics")
customer_log = logging.getLogger("customer.logs")


def _get_fname(request: Request, exception_thrown: bool) -> str:
    _path = request.url.path
    _verb = request.method
    _fname = "NOT_FOUND_404"

    # See: https://github.com/tiangolo/fastapi/issues/861
    # to understand the reasons for the following logic
    routes = request.app.router.routes
    for route in routes:
        match, scope = route.matches(request)
        if match == Match.FULL:
            pt = route.path
            for k in scope["path_params"]:
                pt = pt.replace(f"{{{k}}}", scope["path_params"][k])

            if _path == pt and (_verb in route.methods):
                _fname = route.name
                break

    if exception_thrown and _fname == "NOT_FOUND_404":
        return "500_while_processing_404"

    return _fname


class fastapiMiddleware(BaseHTTPMiddleware):
    """Instrumentation middleware for fastapi."""

    def __init__(self, app):
        """Middleware initialization.

        :param app: the fastapi app.
        """
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        """The actual middleware method.

        :param request: the http-request object.

        :param call_next: the next call object for the middleware.

        :returns: None.
        """
        print("[fastapiMiddleware].dispatch: started")
        exception_thrown = False
        fname = _get_fname(request, exception_thrown)
        request.state.fname = fname

        customer_log.info({"event": f"{fname}.start"})
        # get timestamp
        timestamp_utc = datetime.now(timezone.utc)
        start_time = time.perf_counter_ns()

        response = "Not defined yet"
        try:
            response = await call_next(request)
        except:  # noqa:E722,B001
            exception_thrown = True
            exception_type, exception_value, exception_traceback = sys.exc_info()
            debug_msg = {
                "event": "user-exception",
                "ExceptionClass": f"{type(exception_type)}",
                "ExceptionMessage": f"{exception_value}",
                "ExceptionTraceback": f"{traceback.format_tb(exception_traceback)}",
            }
            print("Unhandled exception captured in the middleware !!!")

            # This is not a Kulshan exception, it's a user exception
            # that we log as an error in the flow
            # customer_log.error(  # noqa: G201
            #     debug_msg,
            #     exc_info=1,
            #     stack_info=True,
            # )

            response = PlainTextResponse("Wow what an error!!", status_code=599)

        end_time = time.perf_counter_ns()
        delta = end_time - start_time
        run_time_ms = ns2ms(delta)

        print(
            f"On '{timestamp_utc.isoformat()}' \"{fname}\" executed in:"
            f" {run_time_ms} milliseconds, with status code: {response.status_code}",
            file=sys.stderr,
        )
        print("[fastapiMiddleware].dispatch: terminated")
        return response
