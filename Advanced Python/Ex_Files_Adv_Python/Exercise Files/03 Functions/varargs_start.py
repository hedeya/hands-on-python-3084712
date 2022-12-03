# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(*parameters):
    result = 0
    for param in parameters:
        result += param
    return result


def main():
    # TODO: pass different arguments
    print(addition(1, 2, 5))
    print(addition(1, 15))
    print(addition(3, 3, 3, 3, 3))
    print(addition(90, 402))

    # TODO: pass an existing list
    myList = [10, 15, 20, 25]
    print(addition(*myList))


if __name__ == "__main__":
    main()
