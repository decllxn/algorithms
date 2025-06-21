#!/usr/bin/python3


# 7. Find the Square Root (Integer Part)
# Difficulty: 45
# Given a number n, find the integer 
# part of its square root using binary search.

n = 40

def integer_square_root(n):
    if n < 2:
        return n

    left, right = 0, n
    result = 0

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == n:
            return mid  # perfect square
        elif square < n:
            result = mid         # save candidate
            left = mid + 1       # search right
        else:
            right = mid - 1      # search left

    return result

print(integer_square_root(n))