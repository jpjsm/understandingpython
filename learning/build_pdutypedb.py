import json

REGIONS = []

with open('regionsdb.json', 'r') as infile:
    REGIONS = json.load(infile)

# Allow a region to be specified by any of its names
INDEXED_REGIONS = {}
for rgn in REGIONS:
    for field in rgn:
        INDEXED_REGIONS[str(field).lower()] = rgn

with open('an_pdu.json', 'r') as infile:
    AN_PDU = json.load(infile)

pdu_typedb = {}
for pdu in AN_PDU:
    region = pdu["location"]["phys"][0:3]
    if region not in INDEXED_REGIONS:
        print "Region code: {0}".format(region)
        print pdu["location"]
        exit()

    r = INDEXED_REGIONS[region][2]

    if r not in pdu_typedb:
        pdu_typedb[r] = {}

    address = pdu["address"]
    pdu_typedb[r][address] = { 'manufacturer':'', 'model':'' , 'name':pdu["name"]}

with open('pdu_typedb.json', 'w') as outfile:
    json.dump(pdu_typedb, outfile, indent=4, separators=(',', ': '))

