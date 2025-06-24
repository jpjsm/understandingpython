#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

for f in os.listdir('testfiles'):
        try:
            with open("testfiles/{}".format(f), 'r') as infile:
                r = infile.read()
        except Exception as e:
            print e

        try:
            with open("testfiles/{}".format(f), 'a') as outfile:
                r = outfile.write(". Successful write.")
        except Exception as e:
            print e
        
