import logsetup
import logging
import sys
import datetime
from os import path as Path

import aboutloggingmodule

# define modulename from file
_modulename_ = Path.splitext(Path.split(Path.splitdrive(__file__)[1])[1])[0]
print(f"_modulename_:{_modulename_}")

# creating module logger
module_logger = logging.getLogger("{0}".format(_modulename_))


def testlogging(arg1, arg2):
    module_logger.info("[%s(%s, %s)] started.", __name__, arg1, arg2)
    aboutloggingmodule.square(arg1)
    aboutloggingmodule.square(arg2)
    aboutloggingmodule.sqrt(arg1)
    aboutloggingmodule.sqrt(arg2)
    module_logger.info("[%s(%s, %s)] completed.", __name__, arg1, arg2)
    return 0


if __name__ == "__main__":
    main_logger = logging.getLogger("main")
    main_logger.setLevel(logsetup.defaultloglevel)
    """
    # connect loggers to real output
    loggers =[]
    modulenames = [_modulename_] + [gbl[0] for gbl in globals().items() if not gbl[0].startswith("__") and isinstance(gbl[1], types.ModuleType)]
    for modulename in modulenames:
        print "... configuring module logger: {0}".format(modulename)
        modulelogger = logging.getLogger(modulename)
        # add the handlers to the logger
        modulelogger.addHandler(fh)
        modulelogger.addHandler(ch)
        loggers.append(modulelogger)
        print ">>>> logging configured for: {0}".format(modulename)
    """

    main_logger.info(f"Arguments received: {sys.argv}")
    if len(sys.argv) == 3:
        main_logger.info(f"About to start 'testlogging({sys.argv[1]}, {sys.argv[2]})'")
        sys.exit(testlogging(sys.argv[1], sys.argv[2]))

    main_logger.warning(f"Wrong number of arguments: {len(sys.argv)-1} != 2")
