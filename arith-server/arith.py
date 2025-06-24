def iseven(n):
    i = int(n)
    return i%2 == 0

def isodd(n):
    return not iseven(n)

def isprime(n):
    i = int(n)
    i = -i if i < 0 else i
    if i == 0:
        return False
    elif i == 1:
        return False
    elif i == 2:
        return True

    j = 2
    while j*j <= i:
        if i % j == 0:
            return False
        j += 1

    return True    
