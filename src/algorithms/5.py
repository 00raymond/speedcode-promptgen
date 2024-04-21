def run(arr):
    prod = 1
    for i in arr:
        if type(i) == str:
            i = ord(i)
        prod *= i
    return prod
# product of all elements in the array