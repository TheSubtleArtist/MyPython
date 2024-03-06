"""
Floor:
Return the floor of the input, element-wise.
This function returns the floor value of the input array elements. The floor of a number x is i if i is the largest integer such that, i<=x. 
The floor function takes a real number x as an input and returns the largest integer that is less than or equal to x.


Ciel:
Return the ceiling of the input, element-wise.
This function returns the ceil value of the input array elements. The floor of a number x is i if i is the smallest integer such that, i>=x

Rint:
Round elements of the array to the nearest integer.

Task:
You are tgiven a 1-D arra, A. Your task is to print the floor, ceil and rint of all the elemnets of A.

Note:
To get the correct output format, add the line numpy.set_printoptions(legacy='1.13')

"""

import numpy
numpy.set_printoptions(legacy='1.13')


A = numpy.array(input().split(), float)

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))