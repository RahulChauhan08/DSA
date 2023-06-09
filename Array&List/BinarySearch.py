def binarySearch(A, n, value):
    start = 0
    end = n-1
    index = search(A, start,end,value)
    if index!=-1:
        return [A[index],index]
    else:
        return ["No value present",index]

def search(A,start,end,value):
    if start < end:
        mid = int((start+end)/2)
        if A[mid] == value:
            return mid
        elif A[mid] > value:
            return search(A,start,mid-1,value)
        else:
            return search(A,mid+1,end,value)
    return -1


A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = binarySearch(A,len(A),120)
print(i)

