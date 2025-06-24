import functools
import time

from werkzeug.exceptions import BadRequest
from flask import Response, Request

static_content = {}

static_content["counters"] = {}
static_content["accumulatedTimers"] = {}

for _key in static_content:
    if fname not in static_content[_key]:
            static_content[_key][fname] = 0

def interceptionAsDecorator(func):
    @functools.wraps(func)
    def wrapper_interceptionAsDecorator(*args, **kwargs):
        fname = func.__name__

        start_time = time.perf_counter_ns()

        value = None

        try:
            value = func(*args, **kwargs)
        except BadRequest as _err:
            print(f"Exception raised: {_err}")
            value = _err

        end_time = time.perf_counter_ns()
        run_time_ms = (end_time - start_time) / 1000000.0
        


