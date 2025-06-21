#!/usr/bin/python3

# Difficulty: 15
# Given a sorted array and a target, return the index if found, else -1.

arr = [1, 3, 5, 7, 9]
target = 7

def search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(search(arr, target))