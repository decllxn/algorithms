#!/usr/bin/python3

# Find All Indices of a Target
# Return a list of all indices where a given value appears.

arr = [1, 2, 3, 2, 4, 2]
target = 2

def indices_of_target(arr, target, count=[]):
    for i in range(len(arr)):
        if arr[i] == target:
            count.append(i)
    return count

print(indices_of_target(arr, target))