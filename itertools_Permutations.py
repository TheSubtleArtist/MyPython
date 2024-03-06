"""
This tool returns successive r length permutations of elements in an iterable.

If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order.
If the input iterable is sorted, the permutation tuples will be produced in a sorted order.

You are given a string .
Your task is to print all possible permutations of size of the string in lexicographic sorted order.

Input Format

A single line of input consisting of the string S .

Output Format

A single line of output consisting of the modified string.

"""

from itertools import permutations

strng, size = input().split()
strng = strng.upper()
permtations = sorted(permutations(strng, int(size)))
for each in permtations:
    print(''.join(each))