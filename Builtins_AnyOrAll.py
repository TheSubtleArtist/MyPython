"""
This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False. 

Task

You are given a space separated list of integers. 
If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format

The first line contains an integer N. 
N is the total number of integers in the list.
The second line contains the space separated list of N integers.


"""

# unnecessary, if needed could aske for len(nList)
n = input()

# must create the list as integers in case there are negative value
nList = list(map(int, input().split()))


if all(i>0 for i in nList):
    print(any(str(x) == str(x)[::-1] for x in nList))
else:
    print('False')



