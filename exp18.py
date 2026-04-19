import numpy as np

# 1D
arr1 = np.array([1, 2, 3, 4])

# 2D
arr2 = np.array([[1, 2], [3, 4]])

# 3D
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D:", arr1)
print("2D:", arr2)
print("3D:", arr3)

# Reshape
print(arr1.reshape(2, 2))

# Slicing
print(arr2[:, 1])

# Indexing
print(arr3[1][0][1])