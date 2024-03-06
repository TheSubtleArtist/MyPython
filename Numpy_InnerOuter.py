"""
INNER:
The inner tool returns the inner product of two arrays.

Outer:
The outer tool returns the outer product of two arrays.

Task:
You are given two arrays: A and B.
Your task is to compute their inner and outer product.

Input Format

The first line contains the space separated elements of array A.
The second line contains the space separated elements of array B.

Output Format:
First, print the inner product.
Second, print the outer product.

"""

import numpy

# In this case, the standard input will provide the arrays. 
# #Because the stdIn provides the arrays separated by '\n' then there is no need to provide a shape n x m
A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A,B), numpy.outer(A,B), sep ='\n')