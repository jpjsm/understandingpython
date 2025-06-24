def isprime(num):
    n = int(num)
    if n < 2:
        raise "Not a positive integer"

    if n == 2:
        return True
    
    i = 2
    while i*i <= n :
        if n % i == 0:
            return False
        i += 1
    
    return True

def findfirstprimes(num):
    n = int(num)
    if n < 2:
        raise "Not a positive integer"

    i = 2
    while i <= n:
        if isprime(i):
            yield i

        i += 1


for prime in findfirstprimes(10000):
    print prime        
