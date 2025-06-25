#!/usr/bin/env python

import multiprocessing
import logging

import pdu_utils
import pdu_scan

import os
import json
import requests
import urllib
import sys
import re
import paramiko
import sshtunnel
import datetime

def get_bastion_endpoint(availabilitydomain, region):
    """
    Builds the enpoint for a bastion at specific region and availability domain.

    Keyword arguments:
    availabilitydomain -- the availability domain number (usually a single digit).
    region -- a list with region name, shortname, aliases

    Returns:
    'bastion-ad{}.{}.oracleiaas.com'
    """
    bastion_endpoint = 'bastion-ad{}.{}.oracleiaas.com'.format(availabilitydomain, region)
    logging.debug('[get_bastion_endpoint(%s, %s)] = %s', availabilitydomain, region, bastion_endpoint)
    return bastion_endpoint


def pdu_testscanner(address):
    logging.debug('[pdu_testscanner(%s)] invoked', address)
    scanresults = pdu_scan.pdu_scan(address)
    logging.debug('[pdu_remotescanner(%s)] = %s', address, scanresults)
    return
if __name__ == "__main__":
    logging.basicConfig(
        filename='pdu_testscanner.log',
        format='%(levelname)s: %(asctime)s %(message)s',
        level=logging.DEBUG) # default level should be INFO
    if len(sys.argv) > 1:
        sys.exit(pdu_testscanner(sys.argv[1]))
