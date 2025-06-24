#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class dictionary(object):
    def __init__(self, definitions):
        with open(definitions, 'r') as infile:
            for l in infile:
                line = l.strip()
                if not line:
                    continue