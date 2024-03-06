"""
https://www.hackerrank.com/challenges/polar-coordinates/problem

Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
Python's cmath module provides access to the mathematical functions for complex numbers.
cmath.phase returns the phase of complex number (also known as the argument of ).

Task
You are given a complex z

. Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number

. Note: complex() function can be used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number

Output Format

Output two lines:
The first line should contain the value of
.
The second line should contain the value of .

"""
import cmath

# the asterisk creates positional arguments, allowing the seperator argument to work.
print(*cmath.polar(complex(input())), sep='\n')