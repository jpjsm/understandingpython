#!/usr/bin/env python

import json
import re

regions = {}
region_index = {}

def save_regions(outputfile='regions.json'):
    if not isinstance(outputfile, str):
        raise 'Argument "outfile" not a string type.'

    rgns = []
    for rgnkey in regions.iterkeys():
        rgn = regions[rgnkey]
        rgns.append('{}"name":"{}","shortname":"{}","aliases":{}{}'.format('{',rgn.name,rgn.shortname if rgn.shortname else '',str(list(rgn.aliases)).replace("'",'"'),'}'))

    with open(outputfile, 'w') as outfile:
        outfile.write('[')
        outfile.write(','.join(rgns))
        outfile.write(']')

def load_regions(inputfile='regions.json'):
    if not isinstance(outputfile, str):
        raise 'Argument "inputfile" not a string type.'

    rgns =json.load(inputfile)
    for rgn in rgns:
        regions[rgn.name]=Region(rgn.name,rgn.shortname,rgn.aliases)

def testforregions(regionlist):
    if not isinstance(regionlist,list):
        if not isinstance(regionlist, str):
            raise 'Argument "regionlist" not a string type.'
        regionlist=[regionlist]

    for region in regionlist:
        if region and region_index.has_key(str(region).lower()):
            return True
    return False        

class Region:
    regionnamepattern = r'^[A-Za-z][A-Za-z0-9_-]*[A-Za-z0-9]$'

    def __init__(self, name, shortname = '', aliases = []):
        assert not testforregions([name,shortname]+(aliases if isinstance(aliases,list) else [str(aliases)])),"Region name, shortname, or one of the aliases is already defined."
        assert name, 'Empty strings or other None equivalents are not allowed'
        assert re.match(self.regionnamepattern,str(name)), "'name' must start with a letter, have one or more letters or digits or dashes or underscores, and end in a letter or digit."
        lowercase_name=name.lower()
        self.name = str(name)
        self.aliases = set([lowercase_name])

        lowercase_shortname=''
        if shortname:
            assert re.match(self.regionnamepattern,str(shortname)), "'shortname', when provided, must start with a letter, have one or more letters or digits or dashes or underscores, and end in a letter or digit."
            self.shortname = str(shortname) 
            lowercase_shortname=shortname.lower()
            self.aliases.add(lowercase_shortname)
        else:
            self.shortname = '' 
                    
        if aliases:
            if not isinstance(aliases,list):
                aliases = [str(aliases)]
            for alias in aliases:
                assert re.match(self.regionnamepattern,alias)
                lowercase_alias=alias.lower()              
                self.aliases.add(lowercase_alias)

        regions[lowercase_name] = self
        for alias in self.aliases:
            region_index[alias] = lowercase_name

    def update_name(self, name):
        assert not testforregions([name]),"New name is already defined."
        assert name, 'Empty strings or other None equivalents are not allowed'
        assert re.match(self.regionnamepattern,str(name)), "'name' must start with a letter, have one or more letters or digits or dashes or underscores, and end in a letter or digit."
        oldname = self.name.lower()
        lowercase_name = name.lower()
        self.aliases.remove(oldname)
        self.name = name
        self.aliases.add(lowercase_name)
        regions.pop(oldname)
        region_index.pop(oldname)
        regions[lowercase_name] = self
        for alias in self.aliases:
            region_index[alias] = lowercase_name

    def update_shortname(self, name):
        assert not testforregions([name]),"New shortname is already defined."
        assert name, 'Empty strings or other None equivalents are not allowed'
        assert re.match(self.regionnamepattern,str(name)), "'shortname' must start with a letter, have one or more letters or digits or dashes or underscores, and end in a letter or digit."
        lowercase_oldshortname = self.shortname.lower()
        lowercase_shortname = name.lower()
        self.aliases.remove(lowercase_oldshortname)
        region_index.pop(lowercase_oldshortname)
        self.shortname = name
        self.aliases.add(lowercase_shortname)
        region_index[lowercase_shortname] = self.name.lower()

    def add_alias(self, alias):
        assert not testforregions([alias]),"New alias is already defined."
        assert alias, 'Empty strings or other None equivalents are not allowed'
        assert re.match(self.regionnamepattern,str(alias)), "'shortname' must start with a letter, have one or more letters or digits or dashes or underscores, and end in a letter or digit."
        self.aliases.add(str(alias).lower())
        region_index[lowercase_shortname] = self.name.lower()

    def remove_alias(self,alias):
        assert not isinstance(alias, type(None)), "None argument not allowed."
        alias_lowercase = str(alias).lower()
        assert (alias_lowercase != self.name.lower()) and (alias_lowercase != self.shortname.lower()), "Cannot remove aliases for name or shortname"
        self.aliases.discard(alias)

    def check_name(self, name):
        return str(name).lower() in self.aliases

             