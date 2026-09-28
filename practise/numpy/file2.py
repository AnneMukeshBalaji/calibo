# Element - wise operations
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print('Array1 + Array2 : ',array1 + array2)
print('Array1 - Array2 : ',array1 - array2)
print('Array1 * Array2 : ',array1 * array2) 
# like you can do all the math operations
matrix1 = np.array([
    [1,2,3],
    [4,5,6]
])
matrix2 = np.array([
    [7,8,9],
    [10,11,12]
])
print(matrix1 @ matrix2.T)
print(np.dot(matrix1,matrix2.T))
