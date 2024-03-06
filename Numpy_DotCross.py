"""
DOT:
The dot tool returns the dot product of two arrays.

CROSS:
The cross tool returns the cross product of two arrays.

Task:
You are given two arrasy A and B. 
Both have dimensions of N x N.
Compute the matrix product.

Input format:
The first line contains the integer N.
The next N lines continas space separated integers of array A
The following N lines contains N space separated integers of array B.

Output format:
print the matrix multiplication of A and B

"""
import numpy
n = int(input())

a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.matmul(a,b))