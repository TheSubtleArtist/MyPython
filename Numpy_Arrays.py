"""
Arrays:
The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.

To use the NumPy module, we need to import it using:

A NumPy array is a grid of values. 
They are similar to lists, except that every element of an array must be the same type.

Task:
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

Input Format:
A single line of input containing space separated numbers.

Output Format:
Print the reverse NumPy array with type float.

Sample Input:
1 2 3 4 -8 -10

Sample Output:
[-10.  -8.   4.   3.   2.   1.]
"""

import numpy

def arrays(arr):
    return numpy.array(arr[::-1], dtype=float)
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)