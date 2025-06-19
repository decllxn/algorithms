#!/usr/bin/python3

# Search for First Occurrence of a Character in a String
# Given a string and a character, return the index of its first occurrence.

text = "interview"
char = "e"

def first_occurence(text, char):
    for i in range(len(text)):
        if text[i] == char:
            return i
    return 'Not found'

print(first_occurence(text, char))