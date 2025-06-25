import json

def get_attribfreq(inarray, outdict):
    for indict in inarray:
        for key in indict:
            if key not in outdict:
                outdict[key] = (0,0)

            attrib_count, attrib_usage = outdict[key]
            attrib_count += 1
            if indict[key] is not None and indict[key] != '':
                attrib_usage += 1
            
            outdict[key] = (attrib_count, attrib_usage)


with open('sk_pdu.json', 'r') as infile:
    SK_PDUS = json.load(infile)

pdu_attributes = {}

get_attribfreq(SK_PDUS, pdu_attributes)

print pdu_attributes