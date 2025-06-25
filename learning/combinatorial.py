#!/usr/bin/env python
# -*- coding: utf-8 -*-

class combinatorial(object):
    def __init__(self, collection):
        if collection is None or not isinstance(collection, list):
            raise Exception('Invalid argument: not a list.')
        self.items = collection

    @staticmethod
    def combinations(collection, size):
        if collection is None or not isinstance(collection, list):
            raise Exception('Invalid argument: not a list.')

        if size < 0 or size > len(collection):
            raise Exception('Invalid argument: value outside range of 0 to {0}.'.format(len(collection)))

        
