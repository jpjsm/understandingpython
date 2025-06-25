import math

def isPrime(n:int)->bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():
    for i in range(100):
        if isPrime(i):
            print(f"{i},", end=' ')
    print()

if __name__ == "__main__":
    main()