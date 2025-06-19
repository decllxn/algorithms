#!/usr/bin/python3

# Search for an element
# Given a list of integers, return the indes of a target number

arr = [10, 25, 39, 40, 5]
target = 40

def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(search(arr, target))