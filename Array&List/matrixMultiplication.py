import numpy as np
def matrixMultiply(mat1,mat2):
    mat3 = []
    for i in range(0,len(mat1)):
        mat3.append(list(np.zeros(len(mat2[0]))))
    if len(mat1[0])==len(mat2):
        for i in range(0,len(mat1)):
            for j in range(0,len(mat2[0])):
                for k in range(0,len(mat2)):
                    mat3[i][j] = mat3[i][j]+ mat1[i][k]*mat2[k][j]
    return mat3


mat1 = [[1,4],[2,5],[3,6]]
mat2 = [[1,2,3],[4,5,6]]
print(matrixMultiply(mat1,mat2))

