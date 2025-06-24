rng = range(0,10)
ascii_digits = zip(range(0,10),[chr(v) for v in range(ord("0"),ord("0")+10)],[[i]*(i+1) for i in range(0,10)])
letters_to_digits = zip([chr(v) for v in range(ord("A"),ord("A")+10)],ascii_digits)
print ascii_digits
print letters_to_digits

for t in letters_to_digits:
    print ">>  {0}".format(t[1])