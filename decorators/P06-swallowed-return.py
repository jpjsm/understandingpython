from decorators06 import do_twice
import sys


@do_twice
def say_hello(name):
    print(f"In '{sys._getframe(0).f_code.co_name}' function")
    return f"Hola {name}"


if __name__ == "__main__":
    hola_Alice = say_hello("Alice")
    print(hola_Alice)
