from decorators10 import repeat


@repeat(num_times=4)
def say_hello(name):
    print(f"Hola {name!r}")


@repeat(6)
def print_dots(num_dots):
    print(f"{'.'*num_dots}")


# Undefined arguments raise an exception
# uncomment next line to see the exception
# @repeat(foo="abc")
def print_colons(num):
    print(f"{':'*num}")


if __name__ == "__main__":
    say_hello("Alice")
    print_dots(3)
    print_colons(2)
