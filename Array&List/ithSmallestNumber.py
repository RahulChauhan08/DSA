def partition(b, p, r):
    i = p
    j = r
    pivot = b[r]
    while True:
        if b[i] < pivot:
            i += 1
        elif b[j] > pivot:
            j -= 1
        if j <= i:
            return j
        b[i], b[j] = b[j], b[i]


def smallestKthNumber(b, p, r, i):
    while r > p:
        q = partition(b, p, r)
        if q == i:
            return b[i]
        elif i < q:
            return smallestKthNumber(b, p, q - 1, i)
        else:
            return smallestKthNumber(b, q + 1, r, i)


A = [10, 40, 20, 50, 60, 70, 100, 90, 80, 30]
print(A)
value = smallestKthNumber(A, 0, len(A) - 1, 8)
print(value)

