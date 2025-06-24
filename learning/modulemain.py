#!/usr/bin/env python

def mod0():
    print "No arguments given"
    return 30

def mod1(arg1):
    print 'One argument --> Arg1 = "{}"'.format(arg1)
    return 31

def mod2(arg1, arg2):
    print 'Two arguments --> Arg1 = "{}"'.format(arg1)
    print 'Two arguments --> Arg2 = "{}"'.format(arg2)
    return 32

def modn(args):
    i = 1
    for arg in args:
         print 'Multiple arguments --> Arg{} = "{}"'.format(i,arg)
         i += 1
    return 33

functionmapper ={
    0:mod0,
    1:mod1,
    2:mod2,
    "default":modn
}
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    print "Total arguments: {}".format(args)
    if args in functionmapper:
        functionmapper[args](sys.argv[1:])
    else:
        functionmapper["default"](sys.argv[1:])
