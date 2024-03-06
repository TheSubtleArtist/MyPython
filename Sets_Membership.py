"""
There is an arry of n integers
There are alos 2 disjoint sets, A and B, each containing m integers.
You like all integers in set A and dislike all integers in set B.
Your initial happiness is 0.
For each "i" integer in the array, if "i" is within A, you add 1 to your happiness.
If "i" is within B, you subtract 1 from your happiness.
Since A and B are sets, they ahve no repeated elements.
The array may contain duplicate elements.
"""

# n and m are useless
n, m = input().split()

# get the ints
ints = input().split()

#take in the two sets, but make sure to set them as sets or the machine may attempt to fool you and stick in one or more duplicates
A = set(input().split())
B = set(input().split())

# list comprehension and takes advantage of true ==1 and false == 0
print(sum((i in A) - (i in B) for i in ints))