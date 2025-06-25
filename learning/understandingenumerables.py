def enumerateitems(sz):
    for i in range(sz):
        yield i

print enumerateitems(10) ## The enumerator, ready to by enumerated

print [enumerateitems(10)] ## A list with the enumerator, ready to by enumerated

print list(enumerateitems(10)) ## The list() enumerates the enumerator

print [j for j in enumerateitems(50) if j%2 == 1]        

enumerations = {
    'all':enumerateitems(10),
    'even':[j for j in enumerateitems(10) if j%2 == 0],
    'odd':[j for j in enumerateitems(10) if j%2 == 1]
}

print enumerations

for i in enumerations['all']:
    if i % 3 == 0:
        print i
