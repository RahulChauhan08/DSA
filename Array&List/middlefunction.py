def middleFun(A):
    A.remove(A[0])
    A.remove(A[len(A)-1])
    return A


A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(middleFun(A))

