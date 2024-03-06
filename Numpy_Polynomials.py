"""
poly: The poly tool returns the coefficients of a polynomial with the given sequence of roots.
roots: The roots tool returns the roots of a polynomial with the given coefficients.
polyint: The polyint tool returns an antiderivative (indefinite integral) of a polynomial
polyder: The polyder tool returns the derivative of the specified order of a polynomial.
polyval: The polyval tool evaluates the polynomial at specific value.
polyfit: The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.

Task
You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.

Input Format
The first line contains the space separated value of the coefficients in P.
The second line contains the value of x.

Output Format
Print the desired value.
"""
import numpy
P = numpy.array(input().split(), float)
x = int(input())
print(numpy.polyval(P, x))

