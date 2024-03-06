"""
MEAN:
The mean tool computes the arithmetic mean along the specified axis. 

VAR:
The var tool computes the arithmetic variance along the specified axis. 

STD:
The std tool computes the arithmetic standard deviation along the specified axis. 

Task:
Given a 2-D Array of size N x M
Find the mean along axis 1
Find the var along axis 0
Find the std along axis NONE

Input format: 
the fist line contains the space separated values of N and M
The next N lines contains the M space separated integers

Output format:
Print the mean
pring the var
print the std
"""

import numpy
n, m = map(int, input().split())
a1 = numpy.array([input().split() for _ in range(n)], int)
#This failed because the STD call does not round the number to the appropriate place
#The correct answer wants 11 digits behind the decimal of STD
print(numpy.mean(a1, axis = 1), numpy.var(a1, axis = 0), numpy.std(a1), sep = "\n")
#worked with added round()
print(numpy.mean(a1, axis=1), numpy.var(a1, axis=0), round(numpy.std(a1, axis = None), 11), sep="\n")




# ----



