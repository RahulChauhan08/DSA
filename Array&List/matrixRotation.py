import numpy as np
def transPose(mat, m, n):
    k = []
    for i in range(0,m):
        k.append(list(np.zeros(n)))
    for i in range(0,m):
        for j in range(0, n):
            k[i][j] = mat[j][i]
    mat = k
    return mat

def reverseMat(mat, m, n):
    k = []
    for i in range(0, m):
        k.append(list(np.zeros(n)))
    for i in range(0, m):
        for j in range(0, n):
            k[i][n-j-1] = mat[i][j]
    mat = k
    return mat


def rotate(mat, m, n, deg):
    i = int(deg/90)
    for j in range(0, i):
        mat = transPose(mat, m, n)
        mat = reverseMat(mat, m, n)
    return mat


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
degree = 90
matrix = rotate(matrix, len(matrix), len(matrix[0]), 90)
print(matrix)
