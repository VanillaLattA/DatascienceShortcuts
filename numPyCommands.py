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
#a.itemsize to find number of bytes
print('\n')

#get a specific part of 2D array
print(array2D[0,0])

print('\n')
#get a specific row
print(array2D[0,:])
print(array2D[1,:])
#same thing works for columns 

#changing things using numPy
array[0]= 1 #replaces with 1

#same thing works for 3D arrays, tip: work outside in


#array creation 
np.full((2,2),3) #create a 2 * 2 filled with 3s

#random numbers
np.random.rand(2,2) # 2 by 2 rand between 0 and 1

#identity matrix
np.identity(5)

#be careful when copying arrays, sometimes the pointers are changed
#this is how you copy 
print("\n")
a= np.array([3])
b= np.array([2])
a = b.copy()
print(b)
#new memory is allocated for b and is not referencing a

print(np.matmul(a,b)) #takes the linear multiplication of 2 variables
#many other functions for linear algebra to find determinant etc


#statistics
np.min(a) # find the min of matrix


print(np.vstack([a,b]))#stacks the array on top of each other
#use hstack for horizontal stack


#Miscellaneous 
#you can index files! check numpy website
