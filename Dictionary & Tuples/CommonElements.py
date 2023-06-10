def commonElements(tup1,tup2):
    ls = []
    for i in tup1:
        if i in tup2:
            ls.append(i)
    return tuple(ls)


tup1 = (1,2,5,6,7,9)
tup2 = (1,10,15,6,7,9)
print(commonElements(tup1,tup2))

