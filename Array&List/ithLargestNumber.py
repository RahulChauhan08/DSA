def largestithNumber(b, p, r, i):
    while p < r:
        q = partition(b, p, r)
        if q == i:
            return b[q]
        elif i > q:
            return largestithNumber(b, q+1, r, i)
        else:
            return largestithNumber(b, p, q-1, i)


def partition(b, p, r):
    pivot = b[r]
    i = p
    j = r
    while True:
        if b[i] < pivot:
            i += 1
        elif b[j] > pivot:
            j -= 1
        if j <= i:
            return j
        b[i], b[j] = b[j], b[i]


A = [10, 40, 20, 50, 60, 70, 100, 90, 80, 30]
print(A)
value = largestithNumber(A, 0, len(A) - 1,len(A)-3)
print(value)