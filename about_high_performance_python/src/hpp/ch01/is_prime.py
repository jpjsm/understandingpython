import math


def IsPrime(number: int) -> bool:
    sqrt_number = math.sqrt(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number % i) == 0:
            return False

    return True
