#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs
import re
definitions = 'e:/GIT/juanpablo.jofre@bitbucket.org/understandingpython/dictionary/definitions.txt'

thumb_letter_prog = re.compile(r"^[A-Za-z]$")
usage_definition_prog = re.compile(r'^Usage\s+(?P<nd>n.\s+.+)$')
usage_alternative_prog = re.compile(r'^[Uu]sage\s+(?P<nd>.+)$')
entry_prog = re.compile(r"^(?P<word>[A-Za-z][A-Za-z'-]+([ -][A-Za-z]+)*[1-9]?)  (?P<definition>((archaic|slang) )?(-?[A-Za-z]+\.)+\s+.+)$")    
entries = {}
n = 0
with codecs.open(definitions, encoding='utf-8') as infile:
    for l in infile:
        n += 1
        line = l.strip().replace(u"\u2014", "-").replace(u"\u2018", "'").replace(u"\u2019", "'")
        if not line:
            continue

        thumb_letter_match = thumb_letter_prog.match(line)
        if thumb_letter_match:
            continue

        usage_definition_match = usage_definition_prog.match(line)
        if usage_definition_match:
            pass
            continue
        usage_alternative_match = usage_alternative_prog.match(line)           
        if usage_alternative_match:
            pass
            continue

        entry_match = entry_prog.match(line)
        if entry_match:
            pass
            continue

        try:
            print  repr(line)#.encode("utf-8")

        except UnicodeEncodeError as ue:
            print "====  Unicode Error ===="
            print "Definitions line #{0}".format(n)
            print ue
            print ue.message
            print ue.reason
            print ue.start, ue.end
            print ue.encoding
            print ue.args
            print "--- ---\n"
            input("... press enter to continue!")
         

# print usage_second_word