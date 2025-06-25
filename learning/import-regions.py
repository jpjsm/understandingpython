#!/usr/bin/env python

import json

with open('regions.json', 'r') as infile:
    regions = json.load(infile)

indexed_regions = {}
for region in regions:
    for field in region:
        indexed_regions[field] = region

for iregion in sorted(indexed_regions.keys()):
    print '{} -> {}'.format(iregion, indexed_regions[iregion])
