"""
MIN:
The tool min returns the minimum value along a given axis.
By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

MAX:
The tool max returns the maximum value along a given axis.
By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array. 

Task: 
You are given a 2-D Array with the dimensions NxM
Your task is to perform the min function over axis 1 and then find the max of that

Input format:
The first line of input contains the space separated values of N and M.
The next N lines contains the M space separated integers
"""

import numpy

N, M = map(int, input().split())

a1 = numpy.array([input().split() for _ in range(N)], int)
a2 = numpy.min(a1, axis=1)
print(numpy.max(a2))

# Also
N, M = map(int, input().split())
print(numpy.max(numpy.min(a1, axis=1)))

#Also
N, M = map(int, input().split())
print(numpy.max(numpy.min(numpy.array([input().split() for _ in range(N)], int), axis=1)))