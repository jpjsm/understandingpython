# Tip calculator

bill = 0.01
while(True):
    bill = input("What's the bill amount? [enter 0 (zero) to terminate] ")
    try:
        bill = float(bill)
        if(bill == 0):
            exit()
        elif (bill < 0):
            print "Bill value should be a positive number."
            continue
        break
    except SystemExit:
        print "Terminated upon user request."
        exit()
    except:
        print "Invalid value, not a number."

print "Bill amount is ${0:.2f}".format(bill)
while(True):
    pct = float(input("What's the desired tip percent? "))
    try:
        pct = float(pct)
        if(pct < 0):
            print "Percentage value should be a positive number."
            continue
        break
    except:
        print "Invalid value, not a number."

tip = bill * pct/100.0
total = bill + tip
print "The tip is ${0:.2f}".format(tip)
print "The total is ${0:.2f}".format(total)