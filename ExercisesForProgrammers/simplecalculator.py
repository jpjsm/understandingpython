# Simple calculator

proceed = raw_input("You'll be asked to enter two numbers.\nDo you want to proceed? [y/n]").lower()
if(not proceed.startswith('y')):
    exit()

while(True):
    a = raw_input('enter first number: ')
    try:
        a = float(a)
        break
    except:
        print "received input is not a valid number"

while(True):
    b = raw_input('enter second number: ')
    try:
        b = float(b)
        break
    except:
        print "received input is not a valid number"

print "{0} + {1} = {2}\n{0} - {1} = {3}\n{0} * {1} = {4}\n{0} / {1} = {5}\n".format(a,b,a+b,a-b,a*b, a/b if b != 0 else '#Div by zero error#')
