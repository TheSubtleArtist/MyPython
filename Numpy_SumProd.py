"""
sum:
The sum tool returns the sum of array elements over a given axis. 

prod:
The prod tool returns the product of array elements over a given axis. 

Task:
You are given a 2-D array with dimension N x M.
Your task is to perform the sum tool over axis 0 and then find the product of that result.


"""

import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
A = numpy.sum(A, axis = 0)
print(numpy.prod(A, axis = 0))

#Also
#print(numpy.prod(numpy.sum(A, axis=0), axis=0)


