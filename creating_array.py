import numpy as np

number = np.array([[1,2,3],[4,5,6]])
print(number)

# creating array 
zeros = np.zeros((3,3)) #3x3 array
print(zeros)

one = np.ones((1,3))
print(one)

full = np.full((5,5), 7) # 5x5 array and fill with value 7
print(full)

identity = np.eye(7) # it will make 7x7 matrics and in identity place it will make 7
print(identity)

arrange = np.arange(1, 10, 2) # start with 1, end with 10 and 2 is jump like 1,3,5...
print(arrange)

linespace = np.linspace(10,100, 5) # it will devide 10 to 100 number in 5 bins
print(linespace)

#--------------------------------------------------------------------------------------------------------------------------

## checking array properties
arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.shape) #(2, 3)
print(arr.size) # 6
print(arr.ndim) # 2 means 2-dimensinal array
print(arr.dtype) # int64

#--------------------------------------------------------------------------------------------------------------------------

## changing datatypes
arr = np.array([1,2,3,4,5], dtype=float)
print(arr.dtype)

arr_int = arr.astype(np.int32)
print(arr_int.dtype) # int32

#--------------------------------------------------------------------------------------------------------------------------

## reshaping and flattening arrays
arr = np.array([[1,2,3],
                [4,5,6]])
print(arr.shape) # (2, 3)

reshape = arr.reshape(3,2)
print(reshape) 
'''
[[1 2]
 [3 4]
 [5 6]] 
 '''

flatten = arr.flatten() # convert 2D into 1D
print(flatten) # [1 2 3 4 5 6] 

#--------------------------------------------------------------------------------------------------------------------------

### Exercizes
# Create an array of 50 random integers between 1 and 100.
arr = np.random.randint(1,100, size=50)
print(arr)

# Create an array of 10 evenly spaced numbers between 0 and 1.
arr = np.linspace(1,10, 2)
print(arr)

# Create a 3x4 array of random integers, then check:
# Shape
# Size
# Number of dimensions (ndim)
# Data type (dtype)
arr1 = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

print(arr1.shape)
print(arr1.size)
print(arr1.ndim)
print(arr1.dtype)

# For the above array, print the maximum, minimum, and mean values.
print(arr.max())
print(arr.min())
print(arr.mean())

# Create an array [10, 20, 30] as integers, then convert it into string type.
arr = np.array([10,20,30])
print(arr.astype(str))

# Create an array of numbers 1 to 12 and reshape it into a 3x4 matrix.
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(3,4))

# Reshape the same array into a 2x2x3 3D array.
print(arr.reshape(2,2,3))

# Convert a 2D array into 1D using both .flatten() and .ravel(). Check if they behave the same when you modify elements.
arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.flatten())
print(arr.ravel())