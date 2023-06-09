def removeDuplicate(A):
    ls=[]
    for i in A:
        if not (i in ls):
            ls.append(i)
    return ls


A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,20,20,30,40,]
print(removeDuplicate(A))


