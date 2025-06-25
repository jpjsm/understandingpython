def parent():
    print("In parent !!")

    def first_child():
        print("In 1st child.")

    def second_child():
        print("In 2nd child.")

    second_child()
    first_child()


if __name__ == "__main__":
    parent()
