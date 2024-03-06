"""
Identity:
The identity tool returns an identity array.
An identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0.
The default type of element is float.

Eye
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. 
The diagnoal can be main, upper, or lower depending on the optiona paramekter  k.
A positive k is for the upper diagonal.
A negative k is for the lower diagonal
A 0 k (default) is for the main diagonal

Task: 
Your task is to print an array of size NxM with its main dagonal elements as 1's and 0's everywhere else

Note: To get alignment corect, please insert the line numpy.set_printoptions(legacy='1.13') below the numpy import

Import format:
A signle line containing space separated values of N and M.
N denotes the rows
M denotes the columns

Output format:
Print the desired NxM array


"""
import numpy
numpy.set_printoptions(legacy='1.13')

#numpy.eye must be used in the solution
#numpy.identity requires only one integer to determine shape
#numpy.eye accounts for the possibility that there is an unexpected change to either the n or m value
n, m = map(int, input().split())
print(numpy.eye(n, m, k=0))