import numpy as np

# indexing
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[0])
print(arr[-1])

# slicing
print(arr[1:5])
print(arr[:8])
print(arr[5:])
print(arr[::2])

# slicing return view not copy
arr[0] = 999
print(arr)

# use .copy() if you need independent copy
arr1 = arr.copy()
arr1[0] = 1
print(arr1)
print(arr)

# Fancy indexing and boolean masking
arr = np.array([10,20,30,40,50])
idx = [0,2,4] # indexis to select
print(arr[idx])

# Boolean masking (filter data)
arr = np.array([10,20,30,40,50,60,70,80,90,100])
filter = arr > 50
print(arr[filter])


## Excersize

# Create a 1D array of numbers 10 to 19.
# Access the first element, last element, and middle element.
arr = np.array([10,11,12,13,14,15,16,17,18,19])
print(arr[0])
print(arr[-1])
print(arr[4])

# Create a 3x3 array with numbers from 1 to 9.
# Access element at row=2, col=3.
# Access the entire 2nd row.
# Access the entire 3rd column.
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr[1,2])
print(arr[1])
print(arr[:,2])

# Create an array of numbers from 0 to 20.
# Slice elements from index 5 to 10.
# Slice every 2nd element from index 2 to 12.
# Slice the last 5 elements.
arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(arr[5:11])
print(arr[2:13:2])
print(arr[:-5])

# Create an array [10, 20, 30, 40, 50, 60, 70].
# Select elements at positions [0, 2, 4].
# Select elements at positions [1, 3, 5].
arr = np.array([10, 20, 30, 40, 50, 60, 70])
idx = [0,2,4]
print(arr[idx])

idx = [1,3,5]
print(arr[idx])

# Create an array of numbers from 1 to 15.
# Select only even numbers.
# Select numbers greater than 10.
# Replace all numbers greater than 10 with -1.
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
even = arr%2 == 0
print(arr[even])

grater = arr > 10
print(arr[grater])

arr[arr>10] = -1
print(arr)






