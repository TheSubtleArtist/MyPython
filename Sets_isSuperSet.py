"""
You are given a set 'A'  and 'n' other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if 'A' is a strict superset of each of the 'n' sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset. 

The first line contains the space separated elements of set .
The second line contains integer , the number of other sets.
The next lines contains the space separated elements of the other sets. 

"""
# inputs the base set
setA = set(map(int, input().split()))

# 'all' returns true if all the items in the set are true. All 'n' sets are evaluated before the print is executed
# '>' is the superset operator
print(all(setA > set(map(int, input().split())) for i in range(int(input()))))