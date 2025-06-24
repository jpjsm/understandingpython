def parent(num):
    def odd_child():
        return "Hi, I'm Odd."

    def even_child():
        return "Hi, I'm Even."

    if num % 2:
        return odd_child

    return even_child


if __name__ == "__main__":
    print("Calling 'parent(1)'")
    p = parent(1)
    print(p, p())
    print("Calling 'parent(2)'")
    p = parent(2)
    print(p, p())
