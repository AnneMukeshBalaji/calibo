import numpy as np

print(np.__version__)

# Creating an array 1D using numpy 
array = np.array([1,2,3,4,5])
print(type(array)) 
# scalar arthemetic 
print('Array + 1 : ',array + 1)
print('Array - 2 : ',array - 2)
print('Array * 3 : ',array * 3)
print('Array / 4 : ',array / 4)
print('Array % 5 : ',array % 5)
print('Array ** 6 : ',array ** 6)
print('Array // 7 : ',array // 7)
# Vectorized operations
# 1] Sqrt function 
print('Sqrt of the function : ',np.sqrt(array))
array = np.array([1.124,125.5,135.99])
# 2] Rounding of the values 
# -> use round to use normal rounding like 0 - 5 round down 6 >= round up
# -> to always round down use np.floor()
# -> to always round up use np.ceil()
print('Array Before Rounding : ',np.round(array))
print('Array Rounding using round method : ',np.round(array))
print('Array Rounding using floor method : ',np.floor(array))
print('Array Rounding using ceil method : ',np.ceil(array))
# EXERCISE Given an radii find the area of the circle 
radii = np.array([1,2,3])
results = radii ** 2 * np.pi
print(results)
# multi - dimensional array
array = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
])
# attributes in numpy 
print('Array Dimesions : ',array.ndim)
print('Shape of the array : ',array.shape)
print('You can do np.pi to use the pi value : ',np.pi)
# Accessing the elements of the array 
print(array[0,1])
# slicing of array in numpy
# array(start:end:step)
print(array[::-1,-1]) 
print(array[::2])

