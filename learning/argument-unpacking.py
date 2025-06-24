# Why Python Is Great:
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

def Add(a,b):
    return a+b

def Substract(c,d):
    return c-d

def AdditiveInverse(x):
    return -x

tuple_vec = (1, 2, 3)
dict_vec = {'x': 1, 'y': 2, 'z': 3}

myfunc(1,2,3)
myfunc(*tuple_vec)
myfunc(**dict_vec)

do_functions = [
    (Add, [9,3]),
    (Substract, [9,3]),
    (AdditiveInverse, [7]),
]

print([_func(*args) for (_func, args) in do_functions])
