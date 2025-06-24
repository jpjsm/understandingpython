import json

def reformat_jsonfile(filename):
    with open(filename, 'r') as infile:
        jsonobjs = json.load(infile)
    with open(filename, 'w') as outfile:
        json.dump(jsonobjs, outfile, indent=4, separators=(',', ': '))

reformat_jsonfile('sk_pdu.json')
reformat_jsonfile('sk_power.json')
reformat_jsonfile('sk_rack.json')
reformat_jsonfile('sk_catalogfull.json')
