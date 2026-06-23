This is a  Numpy tutorial for practising
<br> learning to compare difference between list from python and array from numpy</br>
<br>creating array contains different types of arrays in ehich its easier to make thene from list </br>
<br>different types of datatypes in arrays in numpy</br>
we acess datatype in numpy by dt.type
if we have mixed types in it ,it converts it to float value type

## convert int to float
<br>we use
 arr1 = np.array([1,2,3,4],dtype=np.float32)
ar2= arr_int.astype(np.float64)</br>

## 2 dimensional arrays 
there is like in one array we have arrays more than one like of nested arrays
([[1,2,3,4],[6,7,8,9],[2,3,7,8]])
we can check its shape,size,dimensionsand datatypte
shape by arr.shape,arr.size,arr.ndim,arr.dtype 

## 3 dimensional array

[[[1,2],[3,4],[5,6],[7,8]]]
in this matrix we can attain its size shape and other ndim by same way as in 2d array
## transpose of array
we can also get transpose of arrasy by putting (arr.t)
## different datatypes
int float boolean string
types of int -
.int8
.int16
.int32
.int64
types of float- 
.float16
.float32
.float64
boolean -
bool_
complex datatype-
.complex64
.complex128
## indexing and slicing 
giving or slicing in numpy in one d is same as normal in python 
but in 2d matrix to give indexing we 
use elemnt at row 1 and column 2 we will use
-----matrix[1,2]means row,column 
and to get first row  we use
---------matrix[0,:]
second column
------[ :,1]
acessing elements from matrix in numpy makes easier 