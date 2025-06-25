import logging
import sys

import datetime

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

LOGTIME = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
logfilename = "{0}.{1}.log".format("asyncio_example", LOGTIME)
defaultloglevel = logging.DEBUG
_datefmt = "%Y-%m-%dT%H:%M:%S.%+%z"
# create file handler which logs even debug messages
fh = logging.FileHandler(logfilename)
fh.encoding = "utf-8"
fh.setLevel(defaultloglevel)
fh.name = "FILE"
# create console handler with a higher log level
ch = logging.StreamHandler(stream=sys.stdout)
ch.setLevel(logging.ERROR)
ch.name = "STDOUT"
# create formatter and add it to the handlers
_defaultformat = (
    '{"timestamp": "%(asctime)s", '
    + '"filename": "%(filename)s", '
    + '"functionName": "%(funcName)s", '
    + '"lineno": "%(lineno)d", '
    + '"module": "%(name)s" '
    + '"levelinfo": "%(levelname)s" '
    + '"level": "%(levelno)s" '
    + '"message": "%(message)s"'
)
formatter = logging.Formatter(_defaultformat)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

_handlers = [fh, ch]

logging.basicConfig(
    handlers=_handlers,
    format=_defaultformat,
    datefmt=_datefmt,
    level=defaultloglevel,
    force=True,
)
