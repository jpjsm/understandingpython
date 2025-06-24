#!/usr/bin/env python

import json

## with open('sk_pdu.json', 'r') as infile:
##     PDUS = json.load(infile)

with open('sk_rack.json', 'r') as infile:
    RACKS = json.load(infile)
with open('sk_pdu.json', 'r') as infile:
    PDUS = json.load(infile)
with open('sk_power.json', 'r') as infile:
    POWERS = json.load(infile)

TYPES = {}
for rack in RACKS:
    asset_type = rack["type"]
    if asset_type not in TYPES:
        TYPES[asset_type] = {}
    
    partnum =  rack["part_no"]
    if partnum not in TYPES[asset_type]:
        TYPES[asset_type][partnum] = {}
    
    orapartnum =  asset["part_no"]
    if partnum not in TYPES[asset_type]:
        TYPES[asset_type][partnum] = {}
    
