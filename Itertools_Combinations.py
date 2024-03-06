"""
itertools.combinations(iterable, r)
This tool returns the r length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

"""

import itertools

string, size = input().split()
string = string.upper().strip()
for i in range(1,int(size)+1):
    for each in itertools.combinations(sorted(string),i):
        print(''.join(each))