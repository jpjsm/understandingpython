def say_hello(name) -> str:
    return f"Hello {name}"


def we_are_awesome(name) -> str:
    return f"Hi there, {name}! together we're awesome"


def greet_Bob(greeter_func) -> any:
    return greeter_func("Bob")


if __name__ == "__main__":
    print("Some test cases for: say_hello, we_are_awesome, and greet_Bob")
    print(f"Test 'say_hello(Alice)': {say_hello('Alice')}")
    print(f"Test 'we_are_awesome(Alfred)': {we_are_awesome('Alfred')}")
    print(f"Test 'greet_Bob(say_hello)': {greet_Bob(say_hello)}")
    print(f"Test 'greet_Bob(say_hello)': {greet_Bob(we_are_awesome)}")
