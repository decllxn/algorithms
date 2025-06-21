#!/usr/bin/python3

# Last occurence
# Difficulty 35
# Get last occurence of a duplicate array

arr = [1, 4, 2, 2, 2, 3, 4]
arr.sort()
print(arr)
target = 4


def last_occurence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return result

print(last_occurence(arr, target))