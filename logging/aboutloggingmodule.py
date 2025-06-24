from os import path as Path
import logging

# define modulename from file
_modulename_ = Path.splitext(Path.split(Path.splitdrive(__file__)[1])[1])[0]
print(f"_modulename_:{_modulename_}")

# create module logger
module_logger = logging.getLogger("external.module.{0}".format(_modulename_))
module_logger.handlers = logging.getLogger().handlers


def square(arg1):
    print(
        f"module_logger[{module_logger.name}].handlers: {[hndlr.get_name() for hndlr in module_logger.handlers]}"
    )
    module_logger.info("[%s(%s)] started.", __name__, arg1)
    try:
        index = int(arg1)
    except BaseException as be:
        module_logger.error("[%s(%s)] invalid argument.", __name__, arg1)
        return None

    index *= index
    module_logger.info("[%s(%s)] = %s.", __name__, arg1, index)
    return index


def sqrt(arg1):
    module_logger.info("[%s(%s)] started.", __name__, arg1)
    try:
        index = int(arg1)
    except BaseException as be:
        module_logger.error("[%s(%s)] invalid argument.", __name__, arg1)
        return None

    imaginary = False
    if index < 0:
        imaginary = True
        index = -index
    sqroot = index ** (0.5) if not imaginary else complex(0, index ** (0.5))
    module_logger.info("[%s(%s)] = %s.", __name__, arg1, sqroot)
    return sqroot
