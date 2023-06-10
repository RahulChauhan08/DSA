def maximumKeyValue(dic1):
    max = 0
    key = ''
    for i in dic1.keys():
        if dic1.get(i) > max:
            max = dic1[i]
            key = i
    return [key,max]


dict1={'a':5,'b':9,'c':2}
print(maximumKeyValue(dict1))

