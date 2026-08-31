import numpy as np

arr = np.array([1,2,3,4])
print(arr)
print(arr.ndim)
print(arr.shape)
"""
an array contains a single row of elements it can be termed as one-dimensional array

we can check the dimension using the attribute ndim

eg: print(arr.ndim)
print(arr.shape) --> (4,)  --> number of columns
"""
arr_2 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr_2)
print(arr_2.ndim)
print(arr_2.shape)
"""
an array contain more then 1 rows (rows and columns) like a table format
can be termed as 2-dimensional array

print(arr_2.shape) -->  (2, 4) --> number os rows,number of coumns
"""

arr_3 = np.array([[[1,2,3,4],[5,6,7,8]],
                    [[1,2,3,4],[5,6,7,8]],
                    [[1,2,3,4],[5,6,7,8]]])
print(arr_3)
print(arr_3.ndim)
print(arr_3.shape)
"""
an array contain multiple 2-dimensional arrays

print(arr_3.shape) --> (3, 2, 4) --> 
        
number of 2-dimnsional arrays,number of rows of 2-dimensional array,number of columns of 2-dim array

Zero matrix
=================
matrix with all elements being zero
np.zeros(shape,datatype)
"""
matrix = np.zeros((3,4),dtype=int)
print(matrix)

"""
one matrix
==============
matrix with all elements are 1

"""
matrix_1 = np.ones(shape=(3,5),dtype=int)
print(matrix_1)

"""
full matrix
==============
create a matrix with all elements being a specific value

"""

matrix_2 = np.full(shape=(3,4),fill_value=4,dtype=int)
print(matrix_2)

"""
identity matrix
==================
matrix where rows = column
diagonal elements should be 1 nd other elements filled with 0
n represnts numbr of rows and columns

"""
matrix = np.identity(3,dtype=int)
print(matrix)

print(np.eye(3,dtype=int))

"""
reshape
===========
which means changing the shape of an array without changing its data
i rearrange into rows and columns,dimension
"""

arr = np.array([1,2,3,4,5,6,7,8])
print(arr)

print(arr.reshape(4,2))

arr_2 = np.array([i for i in range(1,9)])
print(arr_2)

arr_3 = np.arange(1,9)
print(arr_3)

arr_3=np.arange(1,9).reshape((2,4))
print(arr_3)

"""
flatten()
===========

converting 2d or 3d array into 1d array

"""
print(arr_3.flatten())

"""
arithmetic operation in arrays
====================================


"""
print()
a = np.array([[1,2,3,4],[5,6,7,8]])
b = np.array([[10,11,12,13],[7,8,9,10]])

print(a+b)
print()
print(a-b)
print()
print(a*b)
print()
print(a/b)
print()
print(a*2) # vector calculation 
# all elements in a array multiplied with 2 an return in new array
print()
print(a+2)
print()
print(a**3)
print()
print(np.add(a,b))
print()
print(np.subtract(a,b))
print()
print(np.multiply(a,b))
print()
print(np.divide(a,b))
print()
print(np.sqrt(a))
print()
print(np.square(a))
print(a % 2)

print(np.sum(a,axis=None)) # add all elements in the array and return the sum
print(np.sum(a,axis=0)) # retuen the sum of elements in column wise
print(np.sum(a,axis=1)) # return the sum of elements in row wise


# sorting
#=================
a = np.array([5,3,6,1,2,10])
print(np.sort(a)) # arrange the eelments in ascending order
print(np.sort(a)[::-1]) # arrange the elements in descending order

# slicing
#============
"""
 0 1 2 3
[1 2 3 4] 0
[5 6 7 8] 1
[7 4 3 2] 2

"""
# arrayname[row_start:row_stop:step,col_start:col_stop:step]

array = np.arange(1,21).reshape(5,4)
print(array)

print(array[2:4,1::])

print()
a = np.array([20,10,30,25,40])
print(np.argsort(a)[::-1]) # return the index positions that would sort the array
print(np.argmax(a)) # return the index of the largest element innthe array

# frrom a 2d array itflatten then return the index position

print(np.argmin(a)) # return the index of smallest element from the array

b = np.array([[3,10,11],[2,5,1],[6,10,4]])
print(b)
print(np.argmax(b))
print(np.argmax(b,axis=1))
print(np.argmax(b,axis=0))

# where 
#============

# find the position of elements those satisfy a condition
# replace the elements

# np.where(condition,value_if_true,value_if_false)

arr =np.array([10,13,15,20,17])
print(np.where(arr >= 15))

b = np.array([[3,10,11],[2,5,1],[6,10,4]])

print(np.sort(b))
print(np.sort(b)[::-1])
print(np.sort(b)[:,::-1])
print(np.sort(b)[::-1,:])
print(np.where(b > 5)) # (array([0, 0, 2, 2]), array([1, 2, 0, 1]))
                                # row index, column index

print(np.where(b > 5,"pass","fail"))

arr = np.array([[30,10,20],
                [60,40,50],
                [90,70,80]])
print(arr)

# axis 1 rowwise

# axis 0 columnwise

# arr[row,col]

print(np.sum(arr,axis=0))
print(arr[:,0:2])
print(arr[0:2,:])
print(arr[::-1,:])
print(arr[:,::-1])
print(arr[::-1,::-1])
print(np.sort(arr)[::-1,::-1])

arr = np.array([1.67,2.5,3.75,4.65])
print(np.round(arr,decimals=1)) # round the number to the neatest integer
print(np.floor(arr)) # floor the decimal numbers to largest number <= the number
print(np.ceil(arr)) # rounds each value up to the nearest greater or equal integer 
                    # (moving towards positive infinity)