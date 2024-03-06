x = int(input("Enter a Number"))
r = x % 2

if r == 0:
    print("Even")
    if x > 10:
        print("You picked a even number larger thant 10")
    else:
        print("You picked and even number less than 10")
else:
    print("Odd")
    if x > 10:
        print("You picked and odd number larger than 10")
    else:
        print("You picked and odd number less than 10")


#The Basis for ElIf

y = int(input("Enter a Number between 1 and 4"))

if y == 1:
    print("One")
if y == 2:
    print("Two")
if y == 3:
    print("Three")
if y == 4:
    print("Four")

# Using ELIF: Only check the following condition if the current condition is FALSE. More efficient coding

elif y == 1:
    print("One")
elif y == 2:
    print("Two")
elif y == 3:
    print("Three")
elif y == 4:
    print("Four")
else:
    print("You entered and inappropriate value")

