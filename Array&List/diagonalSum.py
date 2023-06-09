def diagonalSum(matrix):
    sum = 0
    for i in range(0,len(matrix)):
            sum += matrix[i][i]
    return sum


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonalSum(matrix))

