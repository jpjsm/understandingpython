#!/usr/bin/env python
""""
Gets 'route' ip addresses from static_mappings.json file for region
"""
import os
import ipaddress
import json

basefolder = '/opt/odo-proxy'
an_config = '/opt/autonet-configs'
mappings_rel_location = "etc/ztpserver/files/misc/static_mappings.json"

def get_airport_code():
    '''
    Returns the airport code for current region build
    '''
    with open('/etc/airport') as handle:
        contents = handle.read()
    return contents.strip()

def build_smfilename():
    '''
    Returns the static mapping filename for current region build
    '''
    filename = os.path.join(an_config, get_airport_code(), mappings_rel_location)
    if not os.path.isfile(filename):
        raise Exception('Critical ERROR: static_mappings.json file not found', filename)
    return filename

def load_jsonfile(filename):
    '''
    Returns the static mapping as JSON object, for current region build
    '''
    with open(filename, 'r') as infile:
        return json.load(infile)

def main():
    '''
    Writes the get-ipaddresses.sh file from configuration files
    '''
    ops = load_jsonfile("{0}/odo-proxy-seed.json".format(basefolder))

    ExternalIpAddress = str()
    GreRemote = str()

    sm = load_jsonfile(build_smfilename())
    for route in sm:
        if route["ingress"]["next_hop"] == ops["netconfig"]["LocalNetworkAddress"]:
            ExternalIpAddress = route["route"]
            GreRemote = route["egress"]["next_hop"]
            break

    with open("{0}/get-ipaddresses.sh".format(basefolder), 'w') as outfile:
        outfile.write("# Configure link 0 \n")
        outfile.write("export LocalNetworkAddress={0}\n".format(ops["netconfig"]["LocalNetworkAddress"]))
        outfile.write("export LocalNetworkCIDR={0}\n".format(ops["netconfig"]["LocalNetworkCIDR"]))
        outfile.write("export LocalNetworkGateway={0}\n".format(ops["netconfig"]["LocalNetworkGateway"]))
        outfile.write("\n# External IP address\n")
        outfile.write("export ExternalIpAddress={0}\n".format(ExternalIpAddress))
        outfile.write("\n# Configure gre tunnel\n")
        outfile.write("export GreRemote={0}\n".format(GreRemote))
        outfile.write("export GreLocal={0}\n".format(ops["netconfig"]["GreLocal"]))

if __name__ == '__main__':
    main()
