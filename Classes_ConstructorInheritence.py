'''
Constructor Inheritence
Method Resolution Order

'''

class A:
    def __init__(self):
        print("This is from the A class init")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")

class B:
    def __init__(self):
        print("This is from the B class init")

    def feature3(self):
        print("feature 3")
    def feature4(self):
        print("feature 4")
class C(A,B): # Class and Class B are now superclasses to Class C
    def __init__(self):
        super().__init__()
        print("This is from the C class init")
        #Will not execute the init from class B

    def feature5(self):
        print("feature 5")

    def feature6(self):
        print("feature 6")

class D(A): #A us now the "Super" or "Parent" class for class D (the child or sub class)
    def __init__(self):
        super().__init__()
        #Tells sub class to execute the init of the super class. Super init will be executed first
        print("This is from the D class init")


    def feature7(self):
        print("feature 7")

    def feature8(self):
        print("feature 8")

a1 = A()
print()
b1 = B()
print()
c1 = C()
print()
d1 = D()
print()
c1.feature3() #calling feature three from class B
