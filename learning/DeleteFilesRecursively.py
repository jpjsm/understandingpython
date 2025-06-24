#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re 

def deletefiles(path):
    if os.path.isfile(path):
        os.remove(path)
        return path

    if os.path.isdir(path):
        folder = path
        template = '.*'

    files = os.listdir(path)

    return files


print deletefiles('/Users/jjofre/virtualenvs/learning/python/testfiles/*')