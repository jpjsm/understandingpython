import functools

# define a decorator that has an argument
#


def repeat(num_times):
    """Defines a decorator that has one argument"""

    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kvargs):
            for _ in range(num_times):
                value = func(*args, **kvargs)
            return value

        return wrapper_repeat

    return decorator_repeat
