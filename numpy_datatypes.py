import numpy as np
arr_int =np.array([1,2,3,4,5])
arr_float = np.array([1.0,2.4,5.6])
arr_mixed = np.array([1,2.5,3])

print("integer:",arr_int)
print("float:",arr_float)
print("mixed:",arr_mixed)

arr1 = np.array([1,2,3,4],dtype=np.float32)
ar2= arr_int.astype(np.float64)

print("specified float 32",arr1)
print("specified float 64",ar2)
