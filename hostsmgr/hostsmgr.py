#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re 

class hostsmgr(object):
    
    def __init__(self):
        print 'loading /etc/hosts'

    def validIP4(ip4add):
        

    def LoadFile():
        with open('/etc/hosts', 'r') as infile:
            for line in infile:
                if line.startswith('#'):
                    continue

