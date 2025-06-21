#!/usr/bin/python3

# Search Rotated Index pattern
# Given a rotated array of unique numbers, 
# linearly search for the pivot (smallest number) 
# and return its index.

arr = [5, 6, 7, 8, 1, 2, 3]

def smallest_number(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return (i + 1)
    return 0

print(smallest_number(arr))
