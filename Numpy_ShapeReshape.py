"""
shape:
The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.

reshape:
The reshape tool gives a new shape to an array without changing its data. 
It creates a new array and does not modify the original array itself. 

Task:
You are given a space separated list of nine integers. Your task is to convert this list into a 3 X 3 NumPy array.

Input Format:
A single line of input containing 9 space separated integers.

Output Format:
Print the 3 X 3 NumPy array.

Sample Input:
1 2 3 4 5 6 7 8 9

Sample Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

"""
import numpy as np

print(np.array(input().split(), int).reshape(3,3))