def mergeAndSum(dic1,dic2):
    dic3 = {}
    for i in dic1.keys():
        if not(i in dic3.keys()):
            dic3[i]= dic1[i]
    for i in dic2.keys():
        if not (i in dic3.keys()):
            dic3[i] = dic2[i]
        else:
            dic3[i]=dic3[i]+dic2[i]
    return dic3


dict1 = {'a':1,'b':2,'c':3}
dict2 = {'b':3,'c':4,'d':5}
print(mergeAndSum(dict1,dict2))
