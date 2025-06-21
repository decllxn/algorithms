#!/usr/bin/python3


# Detect Repeating Pattern of K length
# Difficulty 75
# Given a string and an integer k, 
# return True if any substring of length k repeats, 
# otherwise False.

s = "abcdabcde"
k = 4
char = []

def repeating_pattern(s, k):
    for i in range(len(s)):
        if i < k:
            char.append(s[i])
    
    new_char = list(s)
    start_index = k
    end_index = k*2

    char_modif = new_char[start_index:end_index]
    
    if char_modif == char:
        return True
    return False

print(repeating_pattern(s, k))

