#!/usr/bin/env python

import os
import json
import requests
import urllib
import sys
import re
import paramiko
import sshtunnel
import datetime

regions = [
    ['us-tukwila-1', 'r1', 'sea'],
    ['us-phoenix-1', 'r2', 'phx'],
    ['us-ashburn-1', 'us-ashburn-1', 'iad'],
    ['eu-frankfurt-1', 'eu-frankfurt-1', 'fra'],
    ['uk-london-1', 'uk-london-1', 'lon']
    ]

# Allow a region to be specified by any of its names
indexed_regions = {}
for region in regions:
    for field in region:
        indexed_regions[field] = region

def get_bastion_endpoint(ad, region):
    return 'bastion-ad{}.{}.oracleiaas.com'.format(ad, region)

def get_plan_endpoint(ad,region):
    return 'autonet-plan.svc.ad{}.{}'.format(ad, region)

def get_plan_url(port,region,query, page):
    return 'http://localhost:{}/query/?region={}&query={}&page={}'.format(port, region, urllib.quote(query), page)

# Figure out of the name of the PDU (e.g. fra3-...) matches the selected AD
def match_ad(name, ad):
    ad_part = name.split(u'-')[0]
    return ad in ad_part

def ssh_address(address, proxy_command, username, password):
    proxy = paramiko.ProxyCommand(proxy_command)
    client = paramiko.SSHClient()
    try:
        client.connect(
            address, username=username, password=password, sock=proxy, banner_timeout=2, auth_timeout=2)
        print 'connected!'
    except paramiko.SSHException as e:
        print e
    finally:
        client.close()

def datefmt(dt):
    if not isinstance(dt, datetime.datetime):
        raise TypeError("Not a 'datetime.datetime' type:" + str(type(dt)))
    return '{0}-{1:02d}-{2:02d}.{3:02d}.{4:02d}.{5:02d}'.format(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)