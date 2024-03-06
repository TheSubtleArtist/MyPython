# Recursion: Calling a function from within itself
# Maximum recursions is 1000, hardwired
# Recursions can occur if there is an error

import sys
print (sys.getrecursionlimit())
sys.setrecursionlimit(50)
print (sys.getrecursionlimit())
i = 0
def greet():
    global i
    i += 1
    print("Hello ", i)
    greet()

greet()
