def quicksort(b, p, r):
    if p < r:
        q = partition(b, p, r)
        quicksort(b, p, q - 1)
        quicksort(b, q + 1, r)

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


A = [10, 40, 20, 50, 60, 70, 100, 90, 80, 30]
print(A)
quicksort(A, 0, len(A) - 1)
print(A[len(A)-1],A[len(A)-2])
