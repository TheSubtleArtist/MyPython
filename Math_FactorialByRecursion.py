import sys
print (sys.getrecursionlimit())
sys.setrecursionlimit(50)
print (sys.getrecursionlimit())

a = int(input("Please enter a number to apply factorial."))

def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)



result = fact(a)
print(result)