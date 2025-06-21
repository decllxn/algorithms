#!/usr/bin/python3

# 5. Count Occurrences of a Target
# Difficulty: 40
# Return how many times a number appears in a sorted array.

arr = [1, 2, 2, 2, 3, 4]
target = 2

def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Go left for earlier occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Go right for later occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def count_occurrences(arr, target):
    first = find_first(arr, target)
    last = find_last(arr, target)

    if first == -1:
        return 0
    return last - first + 1


arr = [1, 2, 2, 2, 3, 4]
target = 2
print(count_occurrences(arr, target))  # Output: 3
