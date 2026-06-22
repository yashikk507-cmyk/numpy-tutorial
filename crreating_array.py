import numpy as np

arr1 = np.array([1,2,3,4,5])
print("from list:",arr1)

arr2 = np.arange(0,10,2)
print("using arrange:",arr2)

arr3 = np.linspace(0,1,5)#evenly spaced elements
print("using linespace:",arr3)

zeroz = np.zeros(5)#print zeros in array n times as n =5
print("zeros",zeroz)

ones = np.ones(5)#printing ones in array five times
print("ones :",ones)

full = np.full(5,7)
print("sevens in array:",full)

#output
'''from list: [1 2 3 4 5]
using arrange: [0 2 4 6 8]
using linespace: [0.   0.25 0.5  0.75 1.  ]
zeros [0. 0. 0. 0. 0.]
ones : [1. 1. 1. 1. 1.]
sevens in array: [7 7 7 7 7]'''