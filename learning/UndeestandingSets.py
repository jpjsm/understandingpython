foo_set = set([3,4,5])
foo_dict = {1:"uno", 2:"dos", 3:"3"}

print foo_set
print foo_dict

print foo_set & set(foo_dict.keys())
