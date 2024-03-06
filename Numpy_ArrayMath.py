"""
Basic mathematical functions operate element-wise on arrays. 
They are available both as operator overloads and as functions in the NumPy module. 

Task:
You are given two inter arrays, A and B of dimensions N x M.
Your task is to perform the following operations:
add; subtract; multiply; integer division; mod; power.

Note:
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division

Input format: the first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.

Output Format:
Print the results of each operation in the order given under "task";
"""

import numpy

n, m = map(int, input().split())

arrayA = numpy.array([input().strip().split() for x in range(n)], dtype=int)
arrayB = numpy.array([input().strip().split() for x in range(n)], dtype=int)

""" The following produced visibly correct results, but the site said "wrong answer"
print(numpy.add(arrayA, arrayB))
print(numpy.subtract(arrayA, arrayB))
print(numpy.multiply(arrayA, arrayB))
print(numpy.add(arrayA, arrayB))
print(numpy.floor_divide(arrayA, arrayB))
print(numpy.mod(arrayA, arrayB))
print(numpy.power(arrayA, arrayB))
"""

#this worked, no idea why
print(numpy.add(arrayA, arrayB), numpy.subtract(arrayA, arrayB), numpy.multiply(arrayA, arrayB), numpy.floor_divide(arrayA, arrayB), numpy.mod(arrayA, arrayB), numpy.power(arrayA, arrayB), sep='\n')

# Eval also worked
#eval(expression, globals, locals) 
print(*[eval('arrayA' + i + 'arrayB') for i in ['+', '-', '*', '//', '%', '**']], sep = '\n')


