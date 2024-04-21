def run(arr):
    total = 0
    for i in arr:
        if type(i) == str:
            i = ord(i)
        total += i
    return total
# product of all elements in the array
