import numpy as np

arr = np.array([1, 2, 3])
print(np.sum(arr))

array = np.array([[1, 2, 3], [4, 5, 6]])
print("Array original: ")
print(array)
reshape_array = array.reshape(3, 2)
print("Array reshape:")
print(reshape_array)
flatten_array = array.flatten()
print("Array fratten:")
print(flatten_array)
transpose_array = array.transpose()
print("Array transpose:")
print(transpose_array)