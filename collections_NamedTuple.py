"""
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

Referecne: https://www.pythontutorial.net/advanced-python/python-namedtuple/

Example:

from collections import namedtuple

#Point is the name of a the class
# namedtuple is the imported module, but also functions as a superclass
# x and y become field names
Point = namedtuple('Point','x,y')

#pt1 and pt2 become objects of type Point
pt1 = Point(1,2)
pt2 = Point(3,4)

#Now we call values by their field names within the objects
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print dot_product

"""

from collections import namedtuple
from statistics import mean

# will store the values of marks
marks = []

# input the number of students
n = int(input())

# create the headers
Student = namedtuple('Student', input().strip().split())


for _ in range(n):
    # assign input values to each of the header
    student = Student(*input().split())
    # add the student mark to the array
    marks.append(int(student.MARKS))

# find the average, format, and print
    print('{:.2f}'.format(mean(marks)))