#While Loops Rely on some condition

y = int(input("Enter a Number between 5 and 10"))
i = 1

#Increment
while i <= y:
    print ("Fuck Me")
    i = i+1
# Decrement
y=1
while i > y:
    print("Yes")
    i=i-1

#Nested While Loop

m = int(input("Enter a Number between 5 and 10"))
n = 1
p = int(input("Enter a Number between 2 and 4"))
r = 1

while n <= m:
    print ("OH GOD,")
    n = n + 1
    while r <= p:
        print("YES")
        r = r + 1
    r = 1 #resets the value of r before going to the N and M Loop

a = int(input("Enter a Number between 5 and 10"))
b = 1
c = int(input("Enter a Number between 2 and 4"))

while b <= a:
    print ("OH GOD,", end=" ")
    b = b + 1
    d = 1 # initiates the index value inside the while loop each time.
    while d <= c:
        print("YES", end=" ")
        d = d + 1
    print() #Returns to the top of the entire loop, but on next line




