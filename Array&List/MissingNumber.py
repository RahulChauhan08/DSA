def missingNumber(A, n):
    total_sum = (n*(n+1))/2
    sum = 0
    for i in A:
        sum += i
    return int(total_sum-sum)


B = [1, 2, 3, 5, 6]
print(missingNumber(B, 6))
