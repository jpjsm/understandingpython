import multiprocessing
import logging
import datetime
import sys
from socket import gethostname
import pdu_utils
import pdu_scan

loglevel = logging.DEBUG
LOGTIME = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')

logging.basicConfig(
    filename='pdu_localscanner.{0}.{1}.log'.format(gethostname(), LOGTIME),
    format='%(levelname)s: %(asctime)s %(message)s',
    level=loglevel) # default level should be INFO

pdu_scan.pdu_scan('10.144.130.94')

