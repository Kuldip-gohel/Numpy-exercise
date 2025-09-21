import numpy as np
arr = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

print(arr.mean())

print(np.std(arr))

print(np.var(arr)) # compute variance.

print(np.min(arr))
print(np.max(arr))

print(np.sum(arr))
print(np.prod(arr)) # compute product of all element in array

print(np.median(arr))
print(np.percentile(arr, 50)) #For the 50th percentile(median)

print(np.argmin(arr)) # return the index of minimum value in an array.
print(np.argmax(arr))

print(np.corrcoef(arr, arr2)) # Compute corelation coefficient of two arrys

print(np.unique(arr)) # find the unique elements of an array

print(np.diff(arr)) # compute the n-th difference of an array

print(np.cumsum(arr)) # compute the cumulative sum of an array

print(np.linspace(0, 10, 5)) # create an array with evenly spaced numbers over a specified interval.

print(np.log(arr)) # compute the natural logarithm of an array

print(np.exp(arr)) # compute the exponential of an array.



