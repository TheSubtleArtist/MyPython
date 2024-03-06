'''
Method Overloading
-creating two methods with the same name in the same class, but requiring different parameters / arguements
-This is not allowed in pything
Method Overriding
-Creating two methods with the same name, but in different classes
-Is allowed, even if they have the same number argumenets


'''

class student:
    s=0
    def __init__(self, mark1, mark2):
        self.mrk1 = mark1
        self.mrk2 = mark2

    def sum(self, a,b):
        s = a + b
        return s

    def sum2(self, a=None,b=None,c=None): #None allows for the possibliity that a value is not passed to the method. This is as close as it gets to method overloading
        if a!=None and b!=None and c!=None:
            x = a + b + c
        elif a!=None and b!=None:
            x = a + b
        else:
            s=a
        return x

s1 = student(51, 61)

print(s1.sum(5, 9))
print(s1.sum2(1, 2, 3))
print(s1.sum2(5, 10))


#Method Overriding

class A:
    def show(self):
        print("This is Class A")


class B:
    def show(self):
        print("This is Class B")

class C(A):
    pass

class D(A):
    def show(self):
        print("This is Class D")
        #Notice that the show method of the sub class overrides the show method of the super class

a1 = A()
a1.show()
print()
b1 = B()
b1.show()
print()
c1 = C()
c1.show()
print()
d1 = D()
d1.show()


