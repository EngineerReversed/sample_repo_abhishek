
def main(total, numLegs):
    for rabbits in range(total + 1):
        chickens = total - rabbits
        if 2 * chickens + 4 * rabbits == numLegs:
            return chickens, rabbits
    return None, None


if __name__ == '__main__':
    try:
        numHeads = int(raw_input("Input number of heads: "))
        numLegs = int(raw_input("Input number of legs: "))
        result = main(numHeads, numLegs)
        print("Number of chickens are %d and rabbits are %d."%result)
    except TypeError:
        print("TypeError: invalid input")
