import json
import random


def main():
    print("generating file")
    arr = []

    # for each range of number constants, generate like 10 of em (with randomized ranges)

    for i in range(5):
        rand1 = random.randint(0, 25)
        rand2 = random.randint(30, 50)
        op = addtoarr(rand1, rand2)
        for a in op:
            arr.append(a)

    for i in range(5):
        rand1 = random.randint(50, 60)
        rand2 = random.randint(65, 70)
        op = addtoarr(rand1, rand2)
        for a in op:
            arr.append(a)

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(x) for x in range(ord('a'), ord('z') + 1) if chr(x) not in vowels]
    letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]

    for i in range(10):
        arr.append(vowels)
        arr.append(consonants)
        arr.append(letters)

    json_data = json.dumps(arr)

    with open("output/constants.json", "w") as f:
        f.write(json_data)

    return 0


def addtoarr(val1, val2):
    op = []

    oddInts = "odd integers from " + str(val1) + " to " + str(val2) + "."
    oddVals = [x for x in range(val1, val2) if x % 2 != 0]
    op.append((oddInts, oddVals))

    evenInts = "even integers from " + str(val1) + " to " + str(val2) + "."
    evenVals = [x for x in range(val1, val2) if x % 2 == 0]
    op.append((evenInts, evenVals))

    primeInts = "prime integers from " + str(val1) + " to " + str(val2) + "."
    primeVals = [x for x in range(val1, val2) if x > 1 and all(x % i != 0 for i in range(2, x))]
    op.append((primeInts, primeVals))

    div3Ints = "integers divisible by 3 from " + str(val1) + " to " + str(val2) + "."
    div3Vals = [x for x in range(val1, val2) if x % 3 == 0]
    op.append((div3Ints, div3Vals))

    div5Ints = "integers divisible by 5 from " + str(val1) + " to " + str(val2) + "."
    div5Vals = [x for x in range(val1, val2) if x % 5 == 0]
    op.append((div5Ints, div5Vals))

    squareOfInts = "squares of integers from " + str(val1) + " to " + str(val2) + "."
    squareVals = [x ** 2 for x in range(val1, val2)]
    op.append((squareOfInts, squareVals))

    cubeOfInts = "cubes of integers from " + str(val1) + " to " + str(val2) + "."
    cubeVals = [x ** 3 for x in range(val1, val2)]
    op.append((cubeOfInts, cubeVals))

    return op


__main__ = main()
