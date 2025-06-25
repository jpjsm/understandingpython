#!/usr/bin/env python
""""
Gets 'route' ip addresses from static_mappings.json file

Usage:
    python GetProxyInfoFromStaticMappings.py <method> <source> [-d <destination>] [-i <host-ip>]

    method:          'FILE|URL', source is a FILE or a URL
    source:          the location of the static_mappings
    -d destination:  (optional) the location of the proxy-info.json, if different than '/opt/rba-proxy/netconfig-conf/orixy-info.json'
    -i host-ip:      (optional) the host ip to for in the static_mappings object, if different than '172.24.240.29'

"""
import os
import sys
import json
import urllib
import argparse

def usage():
    print >> sys.stderr, """
Usage:
    python GetProxyInfoFromStaticMappings.py <method> <source> [-d <destination>] [-i <host-ip>]

    method:          'FILE|URL', source is a FILE or a URL
    source:          the location of the static_mappings
    -d destination:  (optional) the location of the proxy-info.json, if different than '/opt/rba-proxy/netconfig-conf/orixy-info.json'
    -i host-ip:      (optional) the host ip to for in the static_mappings object, if different than '172.24.240.29'

        """

def load_jsonfile(filename):
    '''
    Returns an object from a JSON file
    '''
    with open(filename, 'r') as infile:
        return json.load(infile)

def webget_jsonfile(jsonurl):
    '''
    Downloads a json formatted object from a url
    '''
    response = urllib.urlopen(jsonurl)
    return json.loads(response.read())

def read_staticmappings(sm, host_ip="172.24.240.29"):
    '''
    Reads a static_mappings structure and returns a proxy-info object
    '''
    proxyinfo = {}
    for route in [ r for r in sm if r["ingress"]["next_hop"] == host_ip ]:
        publicip = route["route"].split('/')[0]
        edgegateway = route["egress"]["next_hop"]
        if "default" not in proxyinfo:
            proxyinfo["default"] = [edgegateway, publicip]

        if edgegateway not in proxyinfo:
            proxyinfo[edgegateway] = [publicip]
        else:
            proxyinfo[edgegateway].append(publicip)

    return proxyinfo

if __name__ == "__main__" :
    destination = '/opt/rba-proxy/netconfig-conf/orixy-info.json'
    parser = argparse.ArgumentParser()
    parser.add_argument("method", help="'FILE|URL', source is a FILE or a URL", choices=["FILE","URL"], type = str.upper)
    parser.add_argument("source", help="the location of the static_mappings")
    parser.add_argument("-d", "--destination", help="(optional) the location of the proxy-info.json, if different than '/opt/rba-proxy/netconfig-conf/orixy-info.json'")
    parser.add_argument("-i", "--ip", help="(optional) the host ip to for in the static_mappings object, if different than '172.24.240.29'")

    args = parser.parse_args()


    if args.method == "FILE":
        staticmappings = load_jsonfile(args.source)
    else:
        staticmappings = webget_jsonfile(args.source)

    if args.destination:
        destination = args.destination

    if args.ip:
        proxyinfo = read_staticmappings(staticmappings, args.ip)
    else:
        proxyinfo = read_staticmappings(staticmappings)

    with open(destination, 'w') as outfile:
        json.dump(proxyinfo, outfile)

