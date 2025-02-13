# use transform functions like sorted, filter, map


def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filterFunc2(x):
    if x == x.upper():
        return True
    return False


def squareFunc(x):
    return x**2


def toGrade(x):
    if x > 90:
        return "A"
    elif x > 80:
        return "B"
    elif x > 70:
        return "C"
    elif x > 65:
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    odds = list(filter(filterFunc, nums))
    print(odds)

    # TODO: use filter on non-numeric sequence
    chars = list(filter(filterFunc2, chars))
    print(chars)

    # TODO: use map to create a new sequence of values
    square = list(map(squareFunc, nums))
    print(square)

    # TODO: use sorted and map to change numbers to grades
    grade = list(map(toGrade, sorted(grades)))
    print(grade)


if __name__ == "__main__":
    main()
