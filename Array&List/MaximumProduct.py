def maxProduct(A):
    max = 0
    index = [0,0]
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            prod = A[i]*A[j]
            if prod>max:
                max=prod
                index[0]=i
                index[1]=j
    return index


A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ind = maxProduct(A)
print(ind,A[ind[0]]*A[ind[1]])
