# Create a 4X2 integer array and Prints its attributes

import numpy as np

firstArray = np.empty([4,2], dtype = np.uint16) 

print(firstArray)

print("shape of the array is: ",firstArray.shape)
print("dimension of the array is: ",firstArray.ndim)
print("itemsize of each element in array is:",firstArray.itemsize)