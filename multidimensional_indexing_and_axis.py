import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr)

# summing along axes
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

# indexing in multidimensional Arrays
print(arr[1, 2])
print(arr[0:2,1:3])

# indexing in 3D array
arr3D = np.array([[[1,2,3], [4,5,6]],
                  [[7,8,9],[11,12,13]]])
print(arr3D.shape)
print(arr3D)

print(arr3D[0,1,2]) # 0->depth, 1->row, 2->column
print(arr3D[:, 0, :])

# changing data along an axis
arr = np.array([[1,2],
                [3,4]])
arr[:, 1] = 0
print(arr)


## Examples

# get all rows of the first column
first_colv = arr3D[:, :, 0]
print(first_colv)

# get the first row from each "sheet" in a 3D array
print(arr3D[:, 0, :])

# create 3x3 array with values from 1 to 9
# Extract sub-matrix [[2,3],[5,6]]. 
# replace 2nd column with [20,50,80].
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr[0:2, 1:3])

arr[1,:] = 20,50,60
print(arr)

# find the maximum value along each row
arr3D = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12]])
row_max = np.max(arr3D, axis=1)
print(row_max)