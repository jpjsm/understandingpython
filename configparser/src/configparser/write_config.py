"""create initial config file for logging in python"""

import configparser

config = configparser.ConfigParser()
config["foo-section"] = {}
config["bar-section"] = {
    "level": "WARNING",
    "logfolder": "./logs",
    "defaultformat": '{"timestamp": "%%(asctime)s", '
    + '"filename": "%%(filename)s", '
    + '"functionName": "%%(funcName)s", '
    + '"lineno": "%%(lineno)d", '
    + '"module": "%%(name)s", '
    + '"levelinfo": "%%(levelname)s", '
    + '"level": "%%(levelno)s", '
    + '"message": "%%(message)s"}',
    "datefmt": "%%Y-%%m-%%dT%%H:%%M:%%S",
    "rotating-filename": "k-rotating.log",
    "rotating-when": "h",
    "rotating-interval": "1",
    "rotating-history": "48",
}

with open("appconfig.ini", "w") as configfile:
    config.write(configfile)
