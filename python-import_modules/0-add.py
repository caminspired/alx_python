if __name__ == "__main__":
    a = 1
    b = 2

    from add_0 import add

    add(a = a, b = b)

    print("{a} + {b} = {sum}".format(a = a, b = b, sum = add(a, b)))
