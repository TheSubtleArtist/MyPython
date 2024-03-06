"""
Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format

The first line contains the string S.
The second line contains the string k.



"""

import re

# Input the String
S = input()

# Input the desired pattern
k = input()

# re.compile communicates that the varialbe contains a regex pattern for ongoing use.
pattern = re.compile(k)

# Search string "S" for the pattern
match = pattern.search(S)

if not match:
    print('(-1, -1)')
else:
    # perform the pattern search as long as there are matches to be found
    while match:
        # print in a tuple format
        # match.start is correlated to the first set of brackets
        # match.end is correlated to the second brackets
        print('({0}, {1})'.format(match.start(), match.end()-1))
        match = pattern.search(S, match.start() + 1)
