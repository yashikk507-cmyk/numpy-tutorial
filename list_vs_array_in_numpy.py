import numpy as np

python_list =[1,2,3,4,5]
numpy_array = np.array([1,2,3,4,5])

print("python list :",python_list)
print("array lsit:",numpy_array)

print("\ntype of python list:",type(python_list))
print("type of array list:",type(numpy_array))

print("adding 10 to each element in list ",[x + 10 for x in python_list] )
print("adding 10 to each element in array",numpy_array + 10)