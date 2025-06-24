from decorators04 import do_twice


@do_twice
def say_hello():
    print("Hola")


if __name__ == "__main__":
    say_hello()
