#!/usr/bin/python3

# 7. Find the First Even Number
# Return the first even number from a list of integers.

arr = [4, 7, 9, 2, 6]


def first_even_number(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            return arr[i]
    return -1

print(first_even_number(arr))