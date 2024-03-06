"""
a right triangle <ABC is 90 degrees at B
Point M is the midpoint of hypotenuse AC
You are given the lenths AB and BC
Your task is to find <MBC, in degrees

Observations:
Point M is the midpoint of hypotenuse AC
Line BM bisects angle <ABC
So: Line AM = line BM = line CM
This divides the right angle triangle into two isoceles triangls
so:  <MBC = <MCB

"""

import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    atan = math.atan2(AB,BC)
    degrees = math.degrees(atan)
    rounded = round(degrees)
    reduced = int(rounded)
    converted = str(reduced)
    symbol = chr(176)
    print(converted+symbol)


    # Really complicated Solution:

import math
if __name__ == '__main__':
        symbol = chr(176)
        print(str(int(round(math.degrees(math.atan2(int(input()), int(input()))))))+symbol)



    




