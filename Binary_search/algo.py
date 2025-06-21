#!/usr/bin/python3

# Binary Search
# The below code is a binary search example

arr = [4, 1, 8, 13, 15, 2, 40, 35, 54, 9]
target = 2

def binary_search(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(binary_search(arr, target))