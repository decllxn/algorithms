#!/usr/bin/python3

# 6. Return Boolean: Is Target Present?
# Return True if a target is present, False otherwise.


arr = ["a", "b", "c", "d"]
target = "b"

def is_present(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

print(is_present(arr, target))