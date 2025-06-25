#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, sys

debug = False

class ParseArguments(object):
    invalidchars_patterns = {
        'name': '[^A-Za-z0-9._-]',
        'file': '[^A-Za-z0-9/._~-]',
        'number': '[^0-9]',
        'ip': '[^0-9.]',
        'uuid': '[^A-Za-z0-9-]',
        'uri': "[^A-Za-z0-9%._~:/?#\[\]@!$&'()*+,;=-]",
        'default': '[^A-Za-z0-9._-]'
    }

    @staticmethod
    def invalidchars(text, kind='default'):
        pattern = ParseArguments.invalidchars_patterns['default']
        if kind in ParseArguments.invalidchars_patterns:
            pattern = ParseArguments.invalidchars_patterns[kind]
        match = re.search(pattern, text)
        result = True if match else False
        if debug and match:
            print "First invalidchar: '{0}'".format(repr(match.group()))
        return result

for kind in ParseArguments.invalidchars_patterns.keys():
    if ParseArguments.invalidchars("", kind):
        print "[ParseArguments] 'invalidchars': Unexpected result testing with empty string for kind: {0}".format(kind)
        sys.exit(10)


# Case: invisible characters in string passed to invalidchars
for kind in ParseArguments.invalidchars_patterns.keys():
    for invisible in ['\a', '\b', '\f', '\n', '\r', '\t', '\v', '\x0a', '\\', '\"', ' ']:
        text = "hello" + invisible
        if not ParseArguments.invalidchars(text, kind):
            print "[ParseArguments] 'invalidchars': Unexpected result testing invisible character ({0}) in string '{1}' passed to invalidchars for kind: {2}".format(repr(invisible), text, kind)
            sys.exit(11)
        text = text + "hello"
        if not ParseArguments.invalidchars(text, kind):
            print "[ParseArguments] 'invalidchars': Unexpected result testing invisible character ({0}) in string '{1}' passed to invalidchars for kind: {2}".format(repr(invisible), text, kind)
            sys.exit(12)
        text = invisible + "hello"
        if not ParseArguments.invalidchars(text, kind):
            print "[ParseArguments] 'invalidchars': Unexpected result testing invisible character ({0}) in string '{1}' passed to invalidchars for kind: {2}".format(repr(invisible), text, kind)
            sys.exit(13)

# Case: valid string cases in invalidchars
test_cases = [
    ("_BU-075.bak", 'name'),
    ("~/_BU-075.bak", 'file'),
    ("987654103", 'number'),
    ("172.24.240.29", 'ip'),
    ("296C52DA-A83C-4209-B05B-2b03eb8341d8", 'uuid'),
    ("https://teamcity.oci.oraclecorp.com/viewType.html?buildTypeId=RegionBuilds_RbaProxySeed_Build&branch_RegionBuilds_RbaProxySeed=userid-rba-1302-validate-name&tab=buildTypeStatusDiv&invisible=[%20]*[+]%._~:/?#@!$&'()*+,;=-;", 'uri'),
    ("_BU-075.bak", 'default'),
]

for test_case in test_cases:
    if ParseArguments.invalidchars(*test_case):
        print "[ParseArguments] 'invalidchars': Unexpected result testing valid string case ({0}) passed to invalidchars for kind: {1}".format(test_case[0], test_case[1])
        sys.exit(14)

print "Successful test."