#!/usr/bin/python3

# Linear Search is used to find an element in a data structure
my_arr = [8, 0, 5, 89, 45, 50, 32, 10, 3]
my_num = 45

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr[i]
    return -1


print(linear_search(my_arr, my_num))