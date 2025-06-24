a = 1.0
b = 1
f = .1
power = 1

while (a + f) != b:
    print "{0: 3} {1: 36.34f}".format(power, f)
    f /= 10.0
    power += 1