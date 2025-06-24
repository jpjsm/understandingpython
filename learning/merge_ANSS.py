
import sys
import json

def make_freqtable(item, freqtabledict):
    if item not in freqtabledict:
        freqtabledict[item] = 0
    freqtabledict[item] += 1

def make_attribfreq(indict, outdict):
    for key in indict:
        if key not in outdict:
            outdict[key] = (0,0)

        attrib_count, attrib_usage = outdict[key]
        attrib_count += 1
        if indict[key] is not None and indict[key] != '':
            attrib_usage += 1
        
        outdict[key] = (attrib_count, attrib_usage)

def get_attribfreq(inarray, outdict):
    for indict in inarray:
        make_attribfreq(indict,outdict)

def print_attribfreq(attribfreqdict, objattribname):
    print "="*96
    print ""
    print "Total different attributes in {0}: {1}".format(objattribname, len(attribfreqdict))
    sorted_keys = attribfreqdict.keys()
    sorted_keys.sort()
    for key in sorted_keys:
        print "\t{0} {1: 7,} {2: 7,} {3: 6.1f}%".format((key + ' '*32)[0:32], attribfreqdict[key][0], attribfreqdict[key][1], (float(attribfreqdict[key][1])/float(attribfreqdict[key][0]))*100.0)

    print ""
    print "_"*96
    print ""

def print_freqtable(freqtabledict, indent=0):
    total = 0
    for frq in sorted([(k, freqtabledict[k]) for k in freqtabledict],key=lambda tpl: tpl[1], reverse=True):
        total += frq[1]
        print ' '*indent + "{0}: {1: 9,}".format((frq[0] + ' '*24)[0:24], frq[1])
    print ' '*indent + "="*35
    print ' '*indent + "{0}: {1: 9,}".format(('Total count' + ' '*24)[0:24], total)

with open('sk_rack.json','r') as infile:
    SK_RACKS = json.load(infile)

with open('sk_pdu.json','r') as infile:
    SK_PDUS = json.load(infile)

with open('sk_power.json','r') as infile:
    SK_POWERUNITS = json.load(infile)

with open('an_devices.json', 'r') as infile:
    AN_DEVICVES = json.load(infile)

with open('an_pdu.json', 'r') as infile:
    AN_PDU = json.load(infile)

with open('an_rack.json', 'r') as infile:
    AN_RACKS = json.load(infile)

sk_rackAttributes = {}
sk_pduAttributes = {}
sk_powerAttributes = {}

children_attributes = {}
rack_childrentype = {}
radr_attributes = {}
rpdu_attributes = {}
rpower_attributes = {}

pdu_adr_attributes = {}
pwr_adr_attributes = {}

get_attribfreq(SK_RACKS, sk_rackAttributes)
get_attribfreq(SK_PDUS, sk_pduAttributes)
get_attribfreq(SK_POWERUNITS, sk_powerAttributes)

for sk_rack in SK_RACKS:
    get_attribfreq(sk_rack['children'], children_attributes)
    make_attribfreq(sk_rack['availability_domain_room'], radr_attributes)

    for rack_child in sk_rack['children']:
        child_type = rack_child['type']
        make_freqtable(child_type, rack_childrentype)

        if child_type == 'pdu':
            make_attribfreq(rack_child, rpdu_attributes)
        elif child_type == 'power':
            make_attribfreq(rack_child, rpower_attributes)


rack_count = len(SK_RACKS)
print "Total racks: {0}".format(rack_count)
print_attribfreq(sk_rackAttributes, 'SK Racks')
print_attribfreq(sk_rackAttributes, 'rack availability_domain_rooms')
print_attribfreq(children_attributes, 'rack children items')
print_attribfreq(rpdu_attributes, 'rack PDU items')
print_attribfreq(rpower_attributes, 'rack Power units')

print "Total different device types in racks: {0}".format(len(rack_childrentype))
sorted_keys = rack_childrentype.keys()
sorted_keys.sort()
print "\t{0} | {1} | {2} | {3}".format(('dev type' + ' '*32)[0:32], '  count', '  racks', 'devices per rack')
print "\t{0}-+-{1}-+-{2}-+-{3}".format('-'*32, '-'*7, '-'*7, '-'*16)
total_devices = 0
for key in sorted_keys:
    type_count = rack_childrentype[key]
    total_devices += type_count
    print "\t{0} | {1: 7,} | {2: 7,} | {3: 9.3f}".format((key + ' '*32)[0:32], type_count, rack_count, (float(type_count)/float(rack_count)))

print "\t{0}-+-{1}-+-{2}-+-{3}".format('-'*32, '-'*7, '-'*7, '-'*16)
print "\t{0} | {1: 7,} | {2: 7,} | {3: 9.3f}".format(('Total' + ' '*32)[0:32], total_devices, rack_count, (float(total_devices)/float(rack_count)))
print ""
print "="*96
print ""


print "Total SK PDUs: {0}".format(len(SK_PDUS))
print_attribfreq(sk_pduAttributes, 'SK PDUs')

freq_skpdu = {
    'parent_type': {},
    'region_name': {},
    'domain_name': {},
    'part_no': {},
    'oracle_part_no': {}
}
for pdu in SK_PDUS:
    make_attribfreq(pdu['availability_domain_room'], pdu_adr_attributes)
    make_freqtable(pdu['parent']['type'], freq_skpdu['parent_type'])
    make_freqtable(pdu['availability_domain_room']['availability_domain_name'], freq_skpdu['domain_name'])
    make_freqtable(pdu['availability_domain_room']['region_name'], freq_skpdu['region_name'])
    make_freqtable(pdu['part_no'], freq_skpdu['part_no'])
    make_freqtable(pdu['oracle_part_no'], freq_skpdu['oracle_part_no'])

print 'SK PDUs:'
print_attribfreq(pdu_adr_attributes, 'PDU Availablity Domain Room')
print '\n    Region frequencies:'
print_freqtable(freq_skpdu['region_name'], 6)
print '\n    Parent Type frequencies:'
print_freqtable(freq_skpdu['parent_type'], 6)
print '\n    Part Number frequencies:'
print_freqtable(freq_skpdu['part_no'], 6)
print '\n    Oracle Part Number frequencies:'
print_freqtable(freq_skpdu['oracle_part_no'], 6)

print "Total SK Power units: {0:,}".format(len(SK_POWERUNITS))
print_attribfreq(sk_powerAttributes, 'SK Power units')

freq_skpwr = {
    'parent_type': {},
    'region_name': {},
    'domain_name': {},
    'part_no': {},
    'oracle_part_no': {}
}

for pwr in SK_POWERUNITS:
    make_attribfreq(pwr['availability_domain_room'], pwr_adr_attributes)
    make_freqtable(pwr['parent']['type'], freq_skpwr['parent_type'])
    make_freqtable(pwr['availability_domain_room']['availability_domain_name'], freq_skpwr['domain_name'])
    make_freqtable(pwr['availability_domain_room']['region_name'], freq_skpwr['region_name'])
    make_freqtable(pwr['part_no'], freq_skpwr['part_no'])
    make_freqtable(pwr['oracle_part_no'], freq_skpwr['oracle_part_no'])

print 'SK Power Units:'
print_attribfreq(pwr_adr_attributes, 'Power Unit Availablity Domain Room')
print '\n    Region frequencies:'
print_freqtable(freq_skpwr['region_name'], 6)
print '\n    Parent Type frequencies:'
print_freqtable(freq_skpwr['parent_type'], 6)
print '\n    Part Number frequencies:'
print_freqtable(freq_skpwr['part_no'], 6)
print '\n    Oracle Part Number frequencies:'
print_freqtable(freq_skpwr['oracle_part_no'], 6)

sys.stdout.flush()