#Creating a blank array and asking for input

from array import *

arr = array("i", [])

n = int(input("Enter number of desired numbers."))

for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)

print(arr)

#Now, manually search the array based on additional user input

a = int(input("Enter number for searching."))
k = 0 #initiaties a variable to represent the index number of the value for which the user is searching

for b in arr:
    if b==a:
        print(k)
        break
    k+=1 #increments k

else:
    print("No values found")


#Now, use functions to search the array based on additional user input
print(arr)
m = int(input("Enter number for searching."))

print(arr.index(m))