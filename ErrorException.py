"""
Handling Exceptions

The statements try and except can be used to handle selected exceptions.
A try statement may have more than one except clause to specify handlers for different exceptions.

Task:
You are given two values a and b
Perform integer division and print a/b

Input:
The first line contains T , the number of test cases.
The next lines each contain the space separated values of a and b.
"""

import sys

T=int(input())

for i in range(T):
	try:
		a, b = map(int, input().split())
		print(a//b)
	except Exception as e:
		print("Error Code:",e)