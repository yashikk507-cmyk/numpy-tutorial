import numpy as np
arr1 = np.array([[1,2,3,4],[6,7,8,9],[2,3,7,8]])
print("type of the array",arr1.dtype)
print("array:",arr1)
print("shape of the array:",arr1.shape)
print("dimension of the array:",arr1.ndim)
print("no. off elemnts in the array",arr1.size)

arr2 = np.array([[[1,2],[3,4,],[5,6],[7,8]]])
print("the 3d array ",arr2)
print("shape of matrix",arr2.shape)
print("size of array",arr2.size)

## to create a random array by giving pramatere
zeros_2d = np.zeros((3,4))
print("\ 2d array",zeros_2d)

ones_3d = np.ones((2,3,4))
print(ones_3d)
print("\n 3d array shape",ones_3d.shape)