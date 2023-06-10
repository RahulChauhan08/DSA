def elementSum(tup1,tup2):
    tup3 = (i+j for i,j in zip(tup1,tup2))
    for i in tup3:
        print(i)


tup1=(1,2,3)
tup2=(4,5,6)
elementSum(tup1,tup2)

