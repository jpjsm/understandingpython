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
import pdu-utils

region = pdu.indexed_regions[sys.argv[1]]
ad = sys.argv[2]

plan_endpoint = pdu.get_plan_endpoint(ad, region[1])
bastion_endpoint = pdu.get_bastion_endpoint(ad, region[1])

# Setup an SSH tunnel through the bastion.  Always use AD1 for the plan service bastion.
print 'Starting SSH tunnel on bastion endpoint: {}; using bind address {}:{}'.format(bastion_endpoint, plan_endpoint, 80)
tunnel = sshtunnel.SSHTunnelForwarder(
    bastion_endpoint,
    remote_bind_address=(plan_endpoint, 80)
)

tunnel.start()
local_plan_port = tunnel.local_bind_port
print '\t->  SSH tunnel started on {} using bastion {}'.format(local_plan_port, bastion_endpoint)

query = 'select address,name from devices where role=\'pdu\''
# Some examples:
#    select name,role,address,location from devices
#    select peer.owner.name,owner.name,name,id from ports where owner.role='cts'
#    select peer.owner.name,owner.name,name,id from ports where owner.role='cts' and peer.owner.name='sea1-pod1-net24-compute1-wic'
#    select name, address, location from devices where role='wic'

print "Using URLs like:"
print pdu.get_plan_url(local_plan_port,region[2],query, 'N')
print
filename="pdu-scanner.pg." + pdu.datefmt(datetime.datetime.now())
try:
    page_number = 1
    devices = []
    while True:
        print 'Querying plan service {} page {}'.format(query, page_number)
        response = requests.get(pdu.get_plan_url(local_plan_port,region[2],query, page_number))
        outfile = file(filename+'pg{0:03d}.txt'.format(page_number),'w')
        outfile.write(response.text)
        outfile.close()
        page = json.loads(response.text)
        for device in page['results']:
            if (pdu.match_ad(device[u'name'], ad)):
                print 'Found PDU {} at {}'.format(device[u'name'], device[u'address'])
                devices.append(device)
            else:
                print 'Skipped PDU {} at {}'.format(device[u'name'], device[u'address'])
        if page_number >= int(page['pages']):
            break
        page_number += 1
finally:
    tunnel.close()

proxy_command = 'ssh {} 2> /dev/null'.format(bastion_endpoint)

# Default Sun PDU username and password
username = 'admin'
password = 'r1P0werP4d'#'adm1n'


# Open an SSH connection to the bastion
print 'Using bastion {}'.format(bastion_endpoint)
bastion_client = paramiko.SSHClient()
bastion_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    bastion_client.connect(bastion_endpoint, banner_timeout=5, auth_timeout=5)
    print 'Connected to bastion {}'.format(bastion_endpoint)
        
    for device in devices:
        print device[u'address']
        _, stdout, stderr = bastion_client.exec_command('ping -w 2 -W 2 {}'.format(device[u'address']))
        result = stdout.read().strip()
        print result
        err = stderr.read().strip()
        print err
        
#    ssh_address(address, proxy_command, username, password)

finally:
    bastion_client.close()

