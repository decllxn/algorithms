#!/usr/bin/python3


# 1. Find Peak Element (Unsorted Array)
# Difficulty: 55
# A peak element is one that is greater than its neighbors. 
# Find the index of any peak.

arr = [1, 3, 20, 4, 1, 0]

def target(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return arr[i]
    return -1

this_target = target(arr)
print(this_target)


def peak_element(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == this_target:
            return mid
        elif arr[mid] > this_target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(peak_element(arr))


# AI version, cleaner and faster

def find_peak(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

print(find_peak(arr))
