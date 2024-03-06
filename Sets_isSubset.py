"""
You are given two sets, A and B.
Your job is to find whether set Ais a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format

The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set .
The second line of each test case contains the space separated elements of set .
The third line of each test case contains the number of elements in set .
The fourth line of each test case contains the space separated elements of set .
"""
# input the number of test cases. 
numTestCase = int(input())

# enter the loop for the number of test cases
for i in range(numTestCase):
    # unnecessary. Inpu the size of the first set 'A'
    setSizeA = int(input())

    # input Set 'A'
    setA = set(map(int, input().split()))

    # unnecessary. Inpu the size of the first set 'B'
    setSizeB = int(input())
     
    # input Set 'B'
    setB = set(map(int, input().split()))

    print(setA.issubset(setB))

