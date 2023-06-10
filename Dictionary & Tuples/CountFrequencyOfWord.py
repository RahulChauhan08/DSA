def countFrequency(words):
    myWordDic = dict()
    for i in words:
        if i in myWordDic.keys():
            myWordDic[i] = myWordDic[i]+1
        else:
            myWordDic[i]=1
    return myWordDic


words = ['apple','orange','banana','apple','orange','apple']
print((countFrequency(words)))


