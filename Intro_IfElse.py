"""
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20 , print Not Weird

"""

import math
import os
import random
import re
import sys


def solveIF(input):
    if (input % 2 == 0) and (n in range(2, 5)):
        return 'Not Weird'
    elif (input % 2 == 0) and (n in range(6, 20)):
        return 'Weird'
    elif (input % 2 == 0) and (n > 20):
        return 'Not Weird'
    else:
        return 'Weird'
    

if __name__ == '__main__':
    n = int(input().strip())
    print(solveIF(n))