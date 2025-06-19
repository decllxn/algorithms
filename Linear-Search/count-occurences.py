#!/usr/bin/python3

# Count Occurrences of a Target
# Given an array, count how many times a target appears.

arr = [2, 4, 4, 1, 4, 5, 4, 4, 4, 3, 6, 9]
target = 4

def count_occurences(arr, target, count=0):
    for i in range(len(arr)):
        if arr[i] == target:
            count+=1
    return count

print(count_occurences(arr, target))