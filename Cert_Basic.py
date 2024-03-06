#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    def __init__(self, max_speed, speed_unit):
        self.mSpeed = max_speed
        self.uSpeed = speed_unit
    
    def cString(self):
        #cDescription = f"Car with the maximum speed of {self.mSpeed} {self.uSpeed}"
        print("Car with the maximum speed of ",self.mSpeed," ", self.uSpeed)
        #print(cDescription.title())
        #return cDescription.title()



class Boat:
    def __init__(self, max_speed):
        self.mSpeed = max_speed
    
    def bString(self):
        #bDescription = f"Boat with the maximum speed of {self.mSpeed} knots"
        print('Boat with the maximum speed of ',self.mSpeed,' knots')
        print(f'Boat with the maximum speed of {self.mSPeed} knots')
        #print(bDescription.title())
        #return bDescription


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
            vehicle.cString()
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
            vehicle.bString()
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()


    <__main__.Car object at 0x7f4365281f70>

    <__main__.Boat object at 0x7f43652a60a0>