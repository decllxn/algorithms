#!/usr/bin/python3

# Difficulty: 30
# Return the index of the first occurrence of the target value.

arr = [1, 4, 2, 2, 2, 3, 4]
target = 2


def first_occurence(arr, target):
    left, right = 0, len(arr) - 1

    index_of_first = arr.index(target)
    new_number = arr[index_of_first]

    while left <= right:
        mid = (left + right) // 2

        if new_number == target:
            return index_of_first
        elif new_number > target:
            left = mid + 1
        else:
            right = mid - 1

print(first_occurence(arr, target))

