"""How to Use Generators and yield in Python.
https://realpython.com/introduction-to-python-generators/
"""


def yielding_numbers(n: int):
    _n = int(n)
    if _n < 0:
        _n = -_n

    for i in range(_n):
        yield i


def yielding_elements_in_list(_thelist):
    for i in _thelist:
        yield i


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


if __name__ == "__main__":
    # numbers_gen = yielding_numbers(0b1 << 24)
    numbers_gen = yielding_numbers(0b1 << 12)
    numbers_count = 0

    for n in numbers_gen:
        numbers_count += 1

    print(f"Numbers count: {numbers_count}")

    # numbers_gen2 = (n for n in range(0b1 << 24))
    numbers_gen2 = (n for n in range(0b1 << 12))
    numbers_count = 0

    for n in numbers_gen2:
        numbers_count += 1

    print(f"Numbers count: {numbers_count}")

    # uncomment to see infinite numbers coming to your screen
    # for j in infinite_sequence():
    #     print(j, end=", ")

    # get the values of the generator individualy
    infinite = infinite_sequence()
    print(next(infinite))
    print(next(infinite))
    print(next(infinite))
    print(next(infinite))

    # Let's see the status of the previous generators
    try:
        print(next(numbers_gen))
    except StopIteration as _exp:
        print(f"StopIteration info {_exp}")
        print(f"StopIteration info {_exp.args}")
        print(f"StopIteration info {_exp.__traceback__}")
    except BaseException as _exp:
        print(f"Exception info {_exp}")
        print(f"Exception info {_exp.args}")
        print(f"Exception info {_exp.__traceback__}")

    try:
        print(next(numbers_gen2))
    except StopIteration as _exp:
        print(f"StopIteration info {_exp}")
        print(f"StopIteration info {_exp.args}")
        print(f"StopIteration info {_exp.__traceback__}")

    # reset generators
    numbers_gen = yielding_numbers(0b1 << 12)
    numbers_gen2 = (n for n in range(0b1 << 12))

    # manualy iterate the generators
    print(next(numbers_gen))
    print(next(numbers_gen))
    print(next(numbers_gen))

    print(next(numbers_gen2))
    print(next(numbers_gen2))
    print(next(numbers_gen2))

    # taking list elements one at a time
    one_at_a_time = yielding_elements_in_list(["1", "a", True, 2, "last"])
    print(next(one_at_a_time))
    print(next(one_at_a_time))
    print(next(one_at_a_time))
    print(next(one_at_a_time))
    print(next(one_at_a_time))
    print(next(one_at_a_time))
