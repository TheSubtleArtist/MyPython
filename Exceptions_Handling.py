'''
Compile time errors
-errors that occur when you ask Python to run the application.
-Before the program can be run, the source code must be compiled into the machine code.
-If the conversion can not perfomed, Python will inform you that your application can not be run before the error is fixed.
-The most common errors of this type are syntax errors – for example, if you don’t end an if statement with the colon.

Runtime errors
-errors that occur after the code has been compiled and the program is running.
-The error of this type will cause your program to behave unexpectedly or even crash.
-An example of an runtime error is the division by zero.

Logical Errors
-everything in the code is syntactically and semantically correct
-desired output is missing because of some logical mistake done by the programmer.
-difficult to find as there is no error thrown by the compiler.
-programmer needs to go through the code to find and correct the error.
-Wrong indentation of the code.
-Solving the expression based on wrong operator precedence.
-Using wrong variable name
-Using the wrong operator to perform the operation.
-Some type errors that lead to data loss in the program.

The goal.... software needs to continue working even when there is an error because the error may only apply to a particluar data or record

'''

a = 10
b = 5
print("resource opened")
print(a/b)
print("This is a correctly executed method")
print("resource closed")
'''
c = 10
d = 0

print(c/d)
print("bye")

e = 10
f = 0

try:
   print(e/f)
except Exception as e: #<-- accepts the error and gives options for what to do next than moves on to the next call
    print("Dividing by zero is not possible")
    print(e)
    print("E/F Exception handled")


g = 10
h = 0

try:
    print("Resource Opened")
    print(g/h) # <--- causes jump to exception handling and does not execute rest of code
    print("This is a correctly executed method")
    print("Resource closed")
except Exception as e: #<-- accepts the error and gives options for what to do next than moves on to the next call
    print("Dividing by zero is not possible")
    print(e)
    print("G/H Exception handled")


i = 10
j = 2

try:
    print("Resource Opened")
    print(i/j) # <--- causes jump to exception handling and does not execute rest of code
    print("This is a correctly executed method")
    print("Resource closed in TRY")
except Exception as e: #<-- accepts the error and gives options for what to do next than moves on to the next call
    print("Dividing by zero is not possible")
    print(e)
    print("Resource closed in Exception") # <-- closing the resource should be done in both the primary function and the exception handling function to prevent compoounding erros
    print("G/H Exception handled")
'''
i = 10
j = 0

try:
    print("Resource Opened")
    print(i/j) # <--- causes jump to exception handling and does not execute rest of code
    print("This is a correctly executed method")
except Exception as e: #<-- accepts the error and gives options for what to do next than moves on to the next call
    print("Dividing by zero is not possible")
    print(e)
    print("G/H Exception handled")
finally:
    print("Resource closed in Finally") # <-closes the connection whether to the method was successful or not
