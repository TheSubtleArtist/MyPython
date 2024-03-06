"""
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet.
If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

#For Example:

from collections import defaultdict

d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print (i)

Task:
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A.
There are m words belonging to word group B.
For each m words, check whether the word has appeared in group A or not.
Print the indices of each m occurrence of in group A.
If it does not appear, print -1 .
"""
from collections import defaultdict
# set up the default dictionary to receive inputs
grpA = defaultdict(list)

# group b will contains the second set of input
# the function must search the deafault dictonary for values in grpB
grpB = []


n, m = map(int, input().split())

for i in range(1, n+1):
    grpA[input()].append(i)

for i in range(m):
    grpB.append(input())

for i in grpB:
    if i in grpA:
        print(' '.join(map(str, grpA[i])))
    else:
        print(str(-1))    
