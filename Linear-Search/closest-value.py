#!/usr/bin/python3

# 2. Search for Closest Value
#  Difficulty: 80

# Given a list of numbers and a target, return the element closest to the target.
# If two are equally close, return the first one.

arr = [4, 1, 8, 13]
target = 15

dict = {}

def closest_value(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr[i]
        else:
            x = target - arr[i]
            dict.update({i: x})
    
    values = list(dict.values())
    for i in range(len(values)):
        values[i] = abs(values[i])
    
    smallest_value = min(values)
    index_of_smallest = values.index(smallest_value)

    return arr[index_of_smallest]


print(closest_value(arr, target))
        
