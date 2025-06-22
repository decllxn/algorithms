#!/usr/bin/python3

# 2. Search in Rotated Sorted Array
# Difficulty: 60
# Given a rotated sorted array with no duplicates,
# search for a target and return its index.

arr = [4, 5, 6, 7, 0, 1, 2]
target = 7


def rotated_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(rotated_array(arr, target))

