#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class SubnetworkRange(object):
    max_32bitint = (2 ** 32) - 1

    def __init__ (self, ip):
        # checking format
        ip = ip.strip()
        # if not re.match(r"[0-9]{1,3}(\.[0-9]{1,3){3}(/[0-9]+)?$",ip):
        m = re.match(r"[0-9]{1,3}(\.[0-9]{1,3}){3}(/[0-9]+)?",ip)
        if not m:
            raise Exception("Invalid IP address") 

        ip = m.group(0)
        address,r = ip.split('/')
        rng = int(r)

        #checking address values
        b = int(0)
        for bt in [ int(a) for a in  address.split('.')]:
            if bt > 255:
                raise "Out of range IP address"
            b = (b << 8) + bt
            
        # checking range
        if not rng:
            rng = 32
        elif rng > 32:
            print "rng: {0}".format(rng)
            raise "Invalid range, must be a number between 1 and 32."

        mask = SubnetworkRange.max_32bitint & (SubnetworkRange.max_32bitint <<(32 - rng))
        bitrng = ~ ((~ SubnetworkRange.max_32bitint) | mask) # Numbers are 64 bit long, need to include upper 64 bits or zeroes will turn into ones
        self.Binary = b
        self.Address = ip
        self.Range = rng
        self.Mask = mask
        self.Net = SubnetworkRange.bin2str(mask & b)
        self.Broadcast = SubnetworkRange.bin2str((mask & b)| bitrng)
        if rng > 30:
            self.Lo = self.Net
            self.Hi = self.Broadcast
        else:
            self.Lo = SubnetworkRange.bin2str((mask & b) + 1)
            self.Hi = SubnetworkRange.bin2str(((mask & b)| bitrng) - 1)

    @staticmethod
    def bin2str(b):
        littlemask = 255
        pieces = ["0","0","0","0"]
        for i in range(3,-1,-1):
            pieces[i] = str(b & littlemask)
            b = b >> 8

        return '.'.join(pieces)
