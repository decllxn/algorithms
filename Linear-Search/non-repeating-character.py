#!/usr/bin/python3

# 1. Find the First Non-Repeating Character
# Difficulty: 75

# Given a string, find the first character that doesn’t repeat. Return its index, or -1.

s = "swiss"

s = "swiss"

# Step 1: Count frequencies
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

print(freq)
# Step 2: Find first unique
for i, char in enumerate(s):
    if freq[char] == 1:
        print(char)  # Output: 0
        break
else:
    print(-1)