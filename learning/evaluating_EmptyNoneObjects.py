target = None
filterList = []

print "target: {0}".format(target)    
print "filterList: {0}".format(filterList)    
print "len(filterList): {0}".format(len(filterList))
if not target==None and len(filterList) != 0 and target in filterList:
    print 'Good'
else:
    print 'Not Good'

print "-"*72
# Changing input

filterList.append(None)

print "target: {0}".format(target)    
print "filterList: {0}".format(filterList)    
print "len(filterList): {0}".format(len(filterList))
if not target==None and len(filterList) != 0 and target in filterList:
    print 'Good'
else:
    print 'Not Good'

print "-"*72
# simplyfing if clause

print "target: {0}".format(target)    
print "filterList: {0}".format(filterList)    
print "len(filterList): {0}".format(len(filterList))
if target and target in filterList:
    print 'Good'
else:
    print 'Not Good'

# Changing input

target = 'target'
filterList = [target]
    