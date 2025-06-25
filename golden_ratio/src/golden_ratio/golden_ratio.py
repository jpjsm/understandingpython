"""Calculating Golden Ratio from Fibonacci series."""
from decimal import Decimal, getcontext

# set max precision for this task
getcontext().prec = 28

fib = [1, 1]
golden = [Decimal("1")]

max_acceptable_error = Decimal("1.0e-10")


def is_close_enough(a: Decimal, b: Decimal) -> bool:
    return abs(a - b) < max_acceptable_error


def is_golden_ratio(a: int, b: int) -> bool:
    if b < a:
        t = b
        b = a
        a = t
    r1 = Decimal(a + b) / Decimal(b)
    r2 = Decimal(b) / Decimal(a)
    return is_close_enough(r1, r2)


def golden_ratio_from_fibonacci():
    while not is_golden_ratio(fib[-2], fib[-1]):
        fib.append(fib[-1] + fib[-2])
        golden.append(Decimal(fib[-1]) / Decimal(fib[-2]))


if __name__ == "__main__":
    golden_ratio_from_fibonacci()
    print(f"Fibonacci numbers required: {len(fib)}")
    print(f"Golden Ratio: {fib[-1]} / {fib[-2]} = {golden[-1]}")
    print(f"Fibonacci numbers         : {fib}")
    print(f"Golden ration convergence : {golden}")
