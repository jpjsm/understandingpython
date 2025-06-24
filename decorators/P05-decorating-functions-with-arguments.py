from decorators05 import do_twice


@do_twice
def greet():
    print("Buenas !!")


@do_twice
def say_hello(name):
    print(f"Hola {name}")


if __name__ == "__main__":
    greet()
    say_hello("Alice")
