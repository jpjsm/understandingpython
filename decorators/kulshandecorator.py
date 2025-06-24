import functools
import logging
from datetime import datetime
from datetime import timezone
import time
import traceback
import sys

# required to implement fastapi middleware
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from kulshan.kmetrics.dimensions import DimensionValuesStarlette
from kulshan.kmetrics.meters import Meters
from kulshan.utils import ns2ms
from kulshan.utils import print_config_if_debug, print_if_debug

# start loggers
kmetrics = logging.getLogger("kulshan.kmetrics")
klogger = logging.getLogger("kulshan.klogging")


def KulshanInstrumentation(func):
    """Instrumentation decorator for Python methods/functions."""

    @functools.wraps(func)
    def wrapper(*args, **kvargs):
        klogger.info({"event": "start"})
        # get timestamp
        timestamp_utc = datetime.now(timezone.utc)
        start_time = time.perf_counter_ns()
        exception_thrown = False

        try:
            value = func(*args, **kvargs)
        except:  # noqa:E722
            exception_thrown = True
            (
                exception_type,
                exception_value,
                exception_traceback,
            ) = sys.exc_info()
            # This is not a Kulshan exception, it's a user exception
            # that we log as an error in the flow
            klogger.error(  # noqa: G201
                {
                    "event": "user-exception",
                    "ExceptionClass": f"{type(exception_type)}",
                    "ExceptionMessage": f"{exception_value}",
                    "ExceptionTraceback": f"{traceback.format_tb(exception_traceback)}",
                },
                exc_info=1,
                stack_info=True,
            )

        end_time = time.perf_counter_ns()
        delta = end_time - start_time
        run_time_ms = ns2ms(delta)

        # Get dimensions values
        klogger.debug({"event": "get-dimension-values.start"})

        fname = func.__name__

        dimension_values = DimensionValuesDecorator.get_dimension_values(
            fname, exception_thrown, timestamp_utc
        )

        klogger.debug({"dimension_values": f"{dimension_values}"})
        klogger.debug({"event": "get-dimension-values.end"})

        # Emit measurements
        klogger.debug({"event": "emit-metric.start"})

        Meters.emit(
            run_time_ms=run_time_ms,
            dimension_values=dimension_values,
        )

        klogger.debug({"event": "emit-metric.done"})

        # Return to middleware caller
        if exception_thrown:
            klogger.info({"event": "finish.with-exception"})
            raise exception_type

        klogger.info({"event": "finish.successful"})
        return value

    return wrapper
