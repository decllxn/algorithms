#!/usr/bin/python3

# 2. Is Target Present? Return True or False
# Difficulty: 20
# Return True if the target exists in the sorted array, otherwise False.

arr = [2, 4, 6, 8, 10]
target = 10

def is_existent(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

print(is_existent(arr, target))