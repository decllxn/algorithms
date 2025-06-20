#!/usr/bin/python3

# Search in a 2D Array
# Find the coordinates (row, col) of a target value in a 2D list.

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
target = 9

def matrix_search(martix, target, count=[]):
    for i in range(len(matrix)):
        if target in matrix[i]:
            count.append(i)
            x = matrix[i]
            for j in range(len(x)):
                if x[j] == target:
                    count.append(j)
    return count

print(matrix_search(matrix, target))