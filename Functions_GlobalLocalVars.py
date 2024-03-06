#Global Variables are created outside of a function
#Global variables can be used both inside of functions and outside.

a = 10 #Global
print(a, id(a))
b = 20
print(b, id(b))
c = 30
print(c, id(c))

def something():
    print("Something1")
    a = 15
    #b = 20
    print("Local", a)
    #print("local", b)

def something2():
    print("Something2")
    print("Local", a)
    print("with no local assignment of the variable 'a', the function takes the value of the global variable")

def something3():
    print("Something3")
    global a
    a = 15
    print("Local", a)
    print("Notice: when the global is pulled in, preference is given to the global")

def something4():
    print("Something4")
    global a
    a = 15
    print("Local", a)
    print("Notice: when the global is pulled in, preference is given to the global")
    a=12
    print("Notice the value of the original global variable has been altered when attempting to create a local variable AFTER the call to the global variable")

def something5():
    print("Something5")
    b = 9
    x = globals()['b']  # gives access to ALL global variables side the function
    print(b, id(x))
    print("Notice the value of 'b' matches the local variable, but the id of 'b' matches the global variable")
    globals()['a'] = 10
    print("We have returned global a to its original value")


something()
something2()
something3()
something4()
print("Global", a)
something5()
print("Global", a)
print()