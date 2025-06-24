#!/bin/python

from os import path as Path
import logging
_modulename_ = Path.splitext(Path.split(Path.splitdrive(__file__)[1])[1])[0]

# creating module logger
module_logger = logging.getLogger(_modulename_)

def name2_foo(a):
    module_logger.debug("in name2_foo")