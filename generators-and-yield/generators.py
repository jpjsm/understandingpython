def first_n_array(n):
    """Build and return a list"""
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


def first_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


def first_n_generator2(n):

    for i in range(n):
        yield i


if __name__ == "__main__":

    print(f"{first_n_array(5)}")
    numbers = first_n_generator(5)
    while True:
        try:
            print(next(numbers))
        except StopIteration:
            break

    for n in first_n_generator2(5):
        print(n)
