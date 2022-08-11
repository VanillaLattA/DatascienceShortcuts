#numpy commands list 
import math
import numpy as np
import collections 


#initialize array 
array = np.array([1,2,3])
print(array)
print('\n')

array2D= np.array([[1.0,2.0],[4.0,5.67]])
print(array2D)
print('\n')

#how to get dimension of array
print(array.ndim)
print(array2D.ndim)

#getting column and width and other values
print(array.shape)
print(array2D.shape)

#you can add function dtype= "int16" in function parameters to specify that it is an int16 type
