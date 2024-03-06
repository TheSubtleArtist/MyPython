

x=input("Enter a number.") #converts inputs to string
y=input("Enter a Number") #converts input to string
a=int(x) #Converts string to int
b=int(y) #Converts string to int
z=x+y
c=a+b
print(z)
print(c)

# More efficient Method

m = int(input("Enter First Number"))
n = int(input("Enter Second Number"))
o=m+n
print(o)

# Inputs as 'Char" format

ch = input("Enter a Character")
print (ch)
print(ch[1])

#Load "char" variable with only one value of the input
hg = input("Enter the next Character.")[0] # Assigns only the first character input to the variable "hg"
print(hg)


#Evaluate the user input; Treats the input as a mathematical function, like a calcualtor

result = eval(input("Enter an Expression"))
print(result)

#argv
import sys
