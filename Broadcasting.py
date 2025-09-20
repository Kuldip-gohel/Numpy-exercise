import numpy as np

# Looping over array in python
# -> This work slow
arr = np.array([1,2,3,4,5])
result = []

for i in arr:
    result.append(i ** 2)

print(result)

# vectorization : Fixing the loop problem
# -> allows you to apply operation to entire array at once
arr = np.array([1,2,3,4,5])
result = arr ** 2 #Vectorized operator
print(result)

# Broadcasting : scaling array without extra memory
arr = np.array([1,2,3,4,5])
result = arr + 10
print(result) # [11 12 13 14 15]
''' Here Scaler 10 is Broadcast across the entire array, and no Extra memory is used.'''

# Broadcasting with arrays of differnt shapes
arr1 = np.array([1,2,3])
arr2 = np.array([99,100,101])
add = arr1 + arr2
print(add)

arr1 = np.array([[1,2,3],
                 [4,5,6]])
arr2 = np.array([1,2,3])
result = arr1 + arr2
print(result)

# Applying broadcasting to real world scenarios
data = np.array([[10,20,30],
                 [15,25,35],
                 [20,30,40],
                 [25,35,45],
                 [30,40,50]])
mean = data.mean(axis=0)
std = data.std(axis=0)

normalized_data = (data - mean) / std

print(normalized_data)


## Examples
#  Given two arrays a = np.array([1,2,3,4]) and b = np.array([10,20,30,40]), use vectorization to compute:
# (a) The element-wise sum.
# (b) The element-wise square of a.
# (c) The dot product of a and b.

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])

sum = a + b
print(sum)

square = a ** 2
print(square)

product = a * b
print(product)

#  Write a NumPy program to compute the Euclidean distance between two points p = (3,4) and q = (7,1) using vectorized operations (without explicit loops).

p = (3,4)
q = (7,1)
Euclidean = ((p[0] - q[0])**2 + (p[1] - q[1])**2) / 2

print(Euclidean)

# Suppose you have an array of student marks:
# marks = np.array([45, 67, 89, 34, 76])
# Using vectorization, increase all marks by 5% and display the updated array.
marks = np.array([45, 67, 89, 34, 76])
increase = ((marks/100)*5) + marks
print(increase)

# Given a 3D array of shape (2,3,4) and a 1D array of shape (4,), show how broadcasting works when you add them. Write the resulting shape.
arr = np.array(
                [[[ 0 , 1 , 2 , 3],
                 [ 4 , 5 , 6 , 7],
                 [ 8 , 9 ,10 ,11]],

                [[12 ,13, 14, 15],
                [16 ,17 ,18, 19],
                [20 ,21 ,22 ,23]]]
                )
array = np.array([10, 20, 30, 40])

add = array + arr 
print(add)
'''
[[[10 21 32 43]
  [14 25 36 47]
  [18 29 40 51]]

 [[22 33 44 55]
  [26 37 48 59]
  [30 41 52 63]]]
'''

# Multiply a column vector
# c = np.array([[1],[2],[3]])
# with a row vector
# r = np.array([10,20,30])
# using broadcasting. What will be the resulting matrix?
c = np.array([[1],[2],[3]])   # shape (3,1)
r = np.array([10,20,30])      # shape (3,)
mul = c * r
print(mul)
'''
[[10 20 30]
 [20 40 60]
 [30 60 90]]
'''