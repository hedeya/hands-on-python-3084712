# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    ftemps1 = [(t*9/5)+32 for t in ctemps]
    ftemps2 = {(t*9/5)+32 for t in ctemps}

    print(ftemps1)
    print(ftemps2)
    # TODO: build a set of unique Fahrenheit temperatures

    # TODO: build a set from an input source
    cTemp = "The quick brown fox jumped over the lazy dog"
    cUp = {c.upper() for c in cTemp if not c.isspace()}
    print(cUp)

if __name__ == "__main__":
    main()
