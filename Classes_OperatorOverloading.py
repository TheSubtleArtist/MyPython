'''
Python operators work for built-in classes.
"int" is a class with certain built in methods
"str" is a class with built-in methods
both "int" and "str" use the "+" sign but in different ways, they have different understandings
user-defined classes do not have the same understanding as built-in classes
overloading is defining those standard methods within the user-defined class
'''

print("Operator Overloading")

class student:

    def __init__(self, mark1, mark2):
        self.mrk1 = mark1
        self.mrk2 = mark2

    def __add__(self, other):  #defines the addition method within the user-defined class
        sum1 = self.mrk1 + other.mrk1
        sum2 = self.mrk2 + other.mrk2
        s3 = student(sum1, sum2)
        return s3

    def __

s1 = student(51, 61)
s2 = student(52, 62)


s3 = s1 + s2

print(s3.mrk1)
print(s3.mrk2)






