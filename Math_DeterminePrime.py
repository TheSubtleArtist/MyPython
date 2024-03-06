#Checking to see if a number is a prime number (inefficient method)

a = int(input("Enter the number you would like to check."))

for i in range(2,a):
    if a % i == 0:
        print(str(a) + " is a not prime number")
        break
else:
    print(str(a) + " is a prime number")