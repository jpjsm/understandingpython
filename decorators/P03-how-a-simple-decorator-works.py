def my_simple_decorator(func):
    def wrapper():
        print(
            "Something is happening BEFORE the function "
            + "'{0}' is called".format(func.__name__)
        )
        func()
        print(
            "Something is happening AFTER the function "
            + "'{0}' was called".format(func.__name__)
        )

    return wrapper


def say_hello():
    print("Hola")


if __name__ == "__main__":
    say_hello = my_simple_decorator(say_hello)
    say_hello()
