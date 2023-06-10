def concateTup(tup):
    s = ''
    for i in tup:
        s = s+" "+i
    return s


tup = ("this","is","hello","world")
print(concateTup(tup))