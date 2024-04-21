def run(arr):
    op = ""
    for c in sorted(arr, reverse=True):
        op += str(c)
    return op

# descending sorted array string concatenation
