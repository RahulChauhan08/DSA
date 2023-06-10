def reverseKeyValue(dic1):
    keys = list(dic1.values())
    value = list(dic1.keys())
    dic = {}
    for i in range(0,len(keys)):
        dic[keys[i]] = value[i]
    return dic


dict1={'a':5,'b':9,'c':2}
print(reverseKeyValue(dict1))

