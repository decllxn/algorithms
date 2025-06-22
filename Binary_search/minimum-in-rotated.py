#!/usr/bin/python3

# Minimum in Rotated Sorted Array
# Difficulty: 65
# Return the minimum element in 
# a rotated sorted array (no duplicates).

arr = [4, 5, 6, 7, -1, 0, 1, 2]

def find_min(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]

print(find_min(arr))