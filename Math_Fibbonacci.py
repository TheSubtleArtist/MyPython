'''a: int = int(input("Enter the Nth value you are seeking"))
if a < 0:
    print("You must select a positive integer")
    a = int(input("Enter the Nth value you are seeking"))

def NthValue(b):
    c = 0
    d = 1
    #print(a)
    #print(b)

    for i in range(2, a):
        e = c + d
        if i == a-1:
            print(e, "is the " + str(a)+"th value of the Fibonacci Sequence")
        c = d
        d = e

NthValue(a)
'''
m: int = int(input("Enter the Upper value you are seeking"))
if m < 2:
    print("You're and idiot choose a bigger number")
    m = int(input("Enter the Nth value you are seeking"))


def UpperBound(n):
    o = 0
    p = 1
    q = 0
    if q < n:
        q = o + p
        o = p
        p = q
    elif q == n:
        print(q)
        print(str(q) + " is the largest value in the Fibonacci Sequence which is still less than " + str(m))
    elif q < n:
        r = q - p
        print(r)
        print(str(r) + " is the largest value in the Fibonacci Sequence which is still less than " + str(m))





        
UpperBound(m)
