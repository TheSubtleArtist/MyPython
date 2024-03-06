"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

For a better understanding of the problem, check the explanation.

Input Format
A single line of input consisting of the string S.

Output Format
A single line of output consisting of the modified string S.

https://www.youtube.com/watch?v=65DeP_qAnX8
"""

from itertools import groupby

strng = input()

# group by goups consecutive items of the same occurraence
# must sort
# failure to sort will result in multiple occurances with different counts of the same key
# Current exercise does not seek sorting, however
# strng = sorted(strng)

# Create the iterable (identifying the keys / unique values which should be sorted together)
# initializes the key and group
groupby(strng)

for key, group in (groupby(strng)):
    print(f'({len(list(group))}, {key})', end=" ")


# Another solutions:

for key, group in (groupby(input())):
    print(f'({len(list(group))}, {key})', end=" ")