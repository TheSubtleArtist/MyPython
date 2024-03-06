"""
zeros

The zeros tool returns a new array with a given shape and type filled with 0's.

Task:
You are given the shape of the array in the form of space-separated integers, 
each integer representing the size of different dimensions, 
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format:
A single line containing the space-separated integers.

Output Format:
First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool. 


numpy.zeros(shape, dtype=float, order='C', *, like=None)
'shape' can be provided as a single int, a list, or a tuple, depending on the situation
"""

import numpy

arrayShape = tuple(map(int, input().split()))
print(numpy.zeros(arrayShape, dtype = int))
print(numpy.ones(arrayShape, dtype = int))
