from os import path as Path
import logging
import understanding_name2

print "__name__: '{0}'".format(__name__)
print "__file__: '{0}'".format(__file__)
print "__package__: '{0}'".format(__package__)
drivename,filepath = Path.splitdrive("/Users/jjofre/Projects/Learning/understandingpython/pdu-scanner.pg.2017-12-01.15.26.13pg001.txt") #__file__
print "Drive:'{0}', file path: '{1}'".format(drivename,filepath)
directorypath, filename = Path.split(filepath)
print "Directory:'{0}', file: '{1}'".format(directorypath, filename)
filewithoutextension,extension = Path.splitext(filename)
print "File name:'{0}', extension: '{1}'".format(filewithoutextension,extension)
_modulename_ = Path.splitext(Path.split(Path.splitdrive(__file__)[1])[1])[0]
print "Module name: {0}".format(_modulename_)

print "Imported module 'understanding_name2' __name__: '{0}'".format(understanding_name2.__name__)

# creating module logger
module_logger = logging.getLogger(_modulename_)

