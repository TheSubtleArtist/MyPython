

a = int(input("Please enter a number to apply factorial."))

def fact(x):
    b = 1
    for i in range(1, x+1): #if you don't use the +1 because indices start from zero, and will terminate at x-1
        b = b * i
    return (b)

result = fact(a)
print(result)