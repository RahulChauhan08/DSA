def pairSum(A,value):
    ls =[]
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]+A[j]==value:
                ls.append([A[i],A[j]])
    return ls


A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(pairSum(A,100))
