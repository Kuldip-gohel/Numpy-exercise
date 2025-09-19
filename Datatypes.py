import numpy as np

# check datatype
arr = np.array([1,2,3,4,5])
print(arr.dtype)

# changing data types
arr = np.array([1.2,1.3,1.5])
print(arr.dtype)

convert = arr.astype(np.int32)
print(convert.dtype)

# why Data types matter in numpy
# --> for memmory usage
arr_int64 = np.array([1,2,3], dtype=np.int64)
arr_int32 = np.array([1,2,3], dtype=np.int32)

print(arr_int64.nbytes) # 24
print(arr_int32.nbytes) # 12

# String Data types
arr = np.array(["apple","mango","Banana"], dtype="U10") # unicode string array
print(arr.dtype)

# complex number
arr = np.array([1 + 2j, 3 + 4j], dtype="complex128")
print(arr.dtype)

# object data type
arr = np.array([{"a":1}, [1,2,3], "hello"], dtype=object)
print(arr.dtype)
