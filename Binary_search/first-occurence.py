#!/usr/bin/python3

# Difficulty: 30
# Return the index of the first occurrence of the target value.

arr = [1, 4, 2, 2, 2, 3, 4]
arr.sort()
print(arr)
target = 2


def first_occurence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return result

print(first_occurence(arr, target))
