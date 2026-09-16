import numpy as np 
arr_id = np.array([1,2,3])
print(arr_id)
print("Array * 2 : ",arr_id * 2) 

# Two Dimensional Array 

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)

# Methods 
# 1] zeroes
new_matrix = np.zeros((2,3))
print(new_matrix)

# Array of Ones 
ones = np.ones((2,3))
print(ones) 

# Array with number 
full_arr = np.full((2,3),7)
print(full_arr)

# Randome Numbers 
random_arr = np.random.random((2,2))
print(random_arr)
