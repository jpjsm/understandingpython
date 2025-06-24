#!/usr/bin/env python
# -*- coding: utf-8 -*-

def addchain(n):
    if not isinstance(n,int):
        raise Exception("Invalid argument data type! Must be integer.")

    if n <= 0:
        raise Exception("Invalid value! Must be a positive number, equal or greater than 1.")

    if n == 1:
        return [(0,"1")]

    