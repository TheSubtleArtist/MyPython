'''
Includes Telusco57, Telusco58
Polymorphism refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
Types of polymorphism:
Duck Typing
Operator Overloading
Method Overloading
Method Overriding
'''


print("Duck typing")
print("If it looks like a duck, quacks like a duck, and swims like a duck, IT'S A DUCK!")
a = 5
print("a=", a)
print(id(a))
a = 'SomeText'
print("a=", a)
print(id(a))
print("Variable names represent memory locations, not values")
print("That's why two values can share the same name and hold different values.")
print()
print()
print()


class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide): #ide is serving as a variable, not as an object
        ide.execute() #this calls a function from the PyCharm Class and works because ide was initiated as a PyCharm object.. .crazy

class MyEditor:
    def execute(self):
        print("Spellcheck")
        print("Syntax Check")
        print("ompiling")
        print("running")

ide = PyCharm()
print()
lap1 = Laptop()
lap1.code(ide) #this is passing and object of class PyCharm to the code method
print()
print()
lap1.code(ide)

