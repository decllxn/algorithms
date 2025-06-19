#!/usr/bin/python3

# Search in a 2D Array
# Find the coordinates (row, col) of a target value in a 2D list.

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
target = 5

def matrix_search(martix, target, count=[]):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i, j] == target:
                count.append(i, j)
    return count

print(matrix_search(matrix, target))