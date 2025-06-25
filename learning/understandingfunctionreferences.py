def Add(a,b):
    return a + b

def Difference(a,b):
    return a - b

def Product(a,b):
    return a * b 

def Division(a,b):
    return a / b

operator2function = {
    '+':Add,
    '-':Difference,
    '*':Product,
    '/':Division
}

left_operands = [9,8,7]
right_operands = [2,3,4]
operators = ['+','-','*','/','%']
for a in left_operands:
    for b in right_operands:
        for op in [o for o in operators if o in operator2function]:
            #  result = map(operator2function[op],[a],[b])
            result = operator2function[op](a,b)
            print "{0} {1} {2} = {3}".format(a,op,b,result)