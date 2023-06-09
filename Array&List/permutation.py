def permutation(A,B):
    if len(A)==len(B):
        for i in A:
            if i in B:
                continue
            else:
                return False
        return True
    else:
        return False


A = [10,20,30,40]
B = [20,10,30,40]
print(permutation(A,B))
