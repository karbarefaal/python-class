import numpy as np

# Create a 1-dimensional NumPy array from a Python list
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)
print("Type of arr1:", type(arr1))
print("Shape of arr1:", arr1.shape) # (5,) indicates 5 elements in one dimension

# Create a 2-dimensional NumPy array (matrix)
arr2 = np.array([[10, 20, 30], [40, 50, 60]])
print("\n2D Array:\n", arr2)
print("Shape of arr2:", arr2.shape) # (2, 3) indicates 2 rows and 3 columns

# Perform element-wise operations
arr_sum = arr1 + 10
print("\nArray after adding 10 to each element:", arr_sum)

# Perform mathematical operations
mean_value = np.mean(arr1)
print("Mean of arr1:", mean_value)

# Array indexing and slicing
print("First element of arr1:", arr1[0])
print("Slice of arr1 (elements from index 1 to 3):", arr1[1:4])
print("Element at row 0, column 1 of arr2:", arr2[0, 1])