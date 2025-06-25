#!/usr/bin/env python

import json

regions = [
    ['us-phoenix-1', 'r2', 'phx'],
    ['us-ashburn-1', 'us-ashburn-1', 'iad'],
    ['eu-frankfurt-1', 'eu-frankfurt-1', 'fra'],
    ['uk-london-1', 'uk-london-1', 'lon']
    ]

with open('regions.json', 'w') as outfile:
    json.dump(regions,outfile,indent=2,separators=(',', ': '))