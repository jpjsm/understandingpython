from decorators07 import do_twice
import sys


@do_twice
def say_hello(name):
    print(f"In '{sys._getframe(0).f_code.co_name}' function")
    return f"Hola {name}"


if __name__ == "__main__":
    hola_Alice = say_hello("Alice")
    print(hola_Alice)

    # The following lines show how decorated functions
    # lose their identities.
    print(
        "In the following lines the 'say_hello' "
        + "function has some identity issues..."
    )
    print("    ... 'say_hello' is now the wrapper function in '@do_twice'")
    print(say_hello)
    print(say_hello.__name__)
    print(help(say_hello))
