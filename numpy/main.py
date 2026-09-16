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

# Random Numbers 
random_arr = np.random.random((2,2))
print(random_arr)

# Identity Matrix 
identity = np.eye(3)
print(identity)

# Array with range of values 
range_arr = np.arange(0,10,2) # Start , Stop , Step 
print(range_arr) 

# Properties / Attributes in Numpy 
# 1] Shape 
print(arr_id.shape,identity.shape) # -> Rows,columns 
# 2]Size
print(identity.size) # -> 9 elements 
# 3]Datatype
print(identity.dtype) # -> int64 / float64
# 4]Number of Dimenstions 
print(identity.ndim) # -> 2 dimensional so 2 

# Accessing Arrays in numpy
array = np.array([1,2,3,4])
print(array[-1])

# Accessing Multi Dimensional Array 
print(matrix[1,2]) # Row , column
