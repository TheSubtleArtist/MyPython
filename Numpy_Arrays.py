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

# Example multi-dimensiontal Array
arrTwoDim = numpy.array([[1,2,3],[9,8,7]], numpy.int8)

# Example Three-dimensional array
arrThreeDim = numpy.array([[[1,2,3],[4,5,6],[7,8,9]],[[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]],[[101,102,103],[104,105,106],[107,108,109]]], numpy.int8)

def arrays(arr):
    return numpy.array(arr[::-1], numpy.float16)
    



if __name__ == '__main__':
    arr = input('Give me some numbers: ').strip().split(' ')
    result = arrays(arr)
    print(result)
    print('TwoDim 0,1: ',arrTwoDim[0,1])
    print('TwoDim 1,1: ', arrTwoDim[1,1])
    print('TwoDim 1,1: ', arrTwoDim[:,1])
    print('TwoDim 1,1: ', arrTwoDim[1,:])

    print('ThreeDim: ', arrThreeDim[0,1,2])
    print("Number of Dimensions in TwoDim: ",arrTwoDim.ndim)
    print("Number of Dimensions in ThreeDim",  arrThreeDim.ndim)
    print("Shape of TwoDim:", arrTwoDim.shape)
    print("Shape of ThreeDim: ",arrThreeDim.shape)
    print("Total number of elements in TwoDim: ",arrTwoDim.size)
    print("Totla Number of elements in ThreeDim: ",arrThreeDim.size)
    print("Data type TwoDim: ", arrTwoDim.dtype)
    print("Data type of ThreeDim: ", arrThreeDim.dtype)
    print("Number of bytes storing TwoDim: ", arrTwoDim.nbytes )
    print("Number of bytes storing ThreeDim: ", arrThreeDim.nbytes)

    # Constants

    print(numpy.inf)
    print(numpy.e)
    print(numpy.pi)
    print(numpy.euler_gamma)


    # Slicing

    arrOneDim = [1,2,3,4,5,6,7,8, numpy.int8]
    print("oneDim:", arrOneDim[1:5])
    print("oneDim:", arrOneDim[-4:-1])
    print("oneDim:", arrOneDim[1:6:2]) # include a step size









