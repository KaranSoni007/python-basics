import numpy as np

# # Part 1 : Multi-dimensional Array

# array = np.array(
#     [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
# )  # No. of elements must be same
# # print(type(array))
# # print(array.ndim)  # Used to find dimensions
# # print(array.shape)  # Used to find no.of depth, rows and columns

# # print(array[0][0][1])  # Chain Indexing

# print(array[1, 1, 2])  # Multi-dimensional Indexing

# word = array[0, 0, 0] + array[1, 0, 0] + array[1, 0, 1]
# print(word)

# Part 2 : Slicing

# array = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8],
#                   [9, 10, 11, 12],
#                   [13, 14, 15, 16]])

# Row Slicing : array[start:end:step]
# print(array[0:4:2])
# print(array[::10])
# print(array[::-1])

# Column Slicing :
# print(array[:, 1:2])
# print(array[:, 1])
# print(array[:, 1::2])
# print(array[:, ::-1])

# print(array[0:2, 0:2])
# print(array[1:3, 1:3])
# print(array[2:3, 3:4])

# Part 3 : Arithmetic operations

# array = np.array([1, 2, 3])
# print(array - 5)

# Vectorized Math Functions

# array = np.array([1, 8, 27])

# print(np.cbrt(array)) # cbrt -> cuberoot; sqrt -> squareroot

# Exercise

# radii = np.array([5, 6, 7])
# print(np.pi * radii ** 2)

# Element wise arithmetic operations

# array1 = np.array([1, 2, 3])
# array2 = np.array([5, 6, 7])

# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1**array2)
# print(array2 // array1)

# Comparison operators

# scores = np.array([80, 90, 73, 89, 78])

# scores[scores < 80] = 0
# print(scores)

# Part 4 : Broadcasting / Matrix Multiplication

# Broadcasting allows numpy to perform operations on arrays with different shapes by virtually expanding dimensions so they match the larger array's shape
# The dimensions have the same size or one of the dimensions has a size of 1

# array1 = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]])
# array2 = np.array([[1],
#                    [2],
#                    [3],
#                    [4]])

# print(array1.shape)
# print(array2.shape)

# print(array1 * array2)

# row = np.array([[10,20], # Matrix Mul.
#                 [20,30], 
#                 [30,40]])
# col = np.array([[1, 2, 3],
#                 [2, 3, 4]
#                 ])
# print(row.shape)
# print(col.shape)
# print(row @ col)

# row = np.array([[10],  # Broadcasting
#                 [20], 
#                 [30]])

# col = np.array([[1, 2, 3]])

# print("row shape:", row.shape)
# print("col shape:", col.shape)
# print(row * col)

# Part 5: Aggregrate functions

# array = np.array([[1, 2, 3, 4, 5],
#                   [6, 7, 8, 9, 10]])
# print(np.sum(array))
# print(np.sum(array, axis = 1)) # axis = 1 -> horizontal
# print(np.sum(array, axis = 0)) # axis = 0 -> vertical
# print(np.mean(array))
# print(np.min(array))
# print(np.max(array))
# print(np.std(array))
# print(np.var(array))
# print(np.argmax(array))
# print(np.argmin(array))

# Part 6 : Filtering

# ages = np.array([[21, 17, 22, 30, 47, 65],
#                  [39, 22, 27, 31, 16,  78]])

# teenagers = ages[ages < 18]
# print(teenagers)

# adults = ages[(ages > 18) | (ages < 60)]
# print(adults)

# senior_citizens = ages[(ages > 60)]
# print(senior_citizens)

# evens = ages[ages % 2 == 0]
# print(evens)

# odds = ages[ages % 2 != 0]
# print(odds)

# Part 7 : Random numbers

range = np.random.default_rng()
print(range.integers(low=1, high=100, size=(3,3)))
print(np.random.uniform(low=-1, high = 1, size=(3,2)))

# Array Reshaping

array = np.array([1, 2, 3, 4, 5, 6, 7, 8])

new_array = array.reshape(2, 4)
print(new_array)