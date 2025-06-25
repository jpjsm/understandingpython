from os import path as Path
import logging
import paramiko


# define modulename from file
_modulename_ = Path.splitext(Path.split(Path.splitdrive(__file__)[1])[1])[0]

# creating module logger
module_logger = logging.getLogger(_modulename_)
module_logger.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s.%(funcName)s: %(message)s')
ch.setFormatter(formatter)

module_logger.addHandler(ch)

usernames = ['alba', 'burt', 'claus', 'dorian']
psswds = ['zulu', 'yak', 'xenon']
ipaddress = '192.168.56.101'

sshclient = paramiko.SSHClient()
for usrnm in usernames:
    for pwd in psswds:
        try:
            step = 10
            sshclient.__init__()
            step = 20
            sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            step = 30
            sshclient.connect(ipaddress,username=usrnm, password=pwd,allow_agent=False,look_for_keys=False)
            print "connected using: {0}/{1}"
        except paramiko.SSHException as sshx:
            module_logger.debug(
                '[try_defaultcredentials(%s, %s, %s)]: step %s\n\t(1) Unknown paramiko exception:%s\n\t(2) Arguments: %s',
                ipaddress,
                usrnm,
                pwd,   
                step,                 
                sshx.message,
                sshx.args)
        finally:
            sshclient.close()
