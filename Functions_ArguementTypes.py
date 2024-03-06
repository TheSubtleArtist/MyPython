
print("Positional Arguements")
print("Please provide two numbers")
c = int(input())
d = int(input())

def add(a, b):
    e = a + b
    print(e)

add(c, d)

print("a and b are positional arguements, their values are dependant on the position of the arguements passed to them.")

print("Keyword Arguments")
f = input("Please provide the person's name")
g = input("Please provide the person's age")

def person (name, age):
    print(name)
    print(age)

print("if the user inputs the information incorrectly? Use Keywords to assign input to the argumenets")
#key words are name and age, set to to the input value from the user
person(name = f, age = g)


print("Default Arguements, but I am having a hard time getting this to work")


h = input("Please provide the person's name")
i = input("Please provide the person's age")

def person (name2, age2):
    print(name2)
    print(age2)


print("What if the user only provides one of the requested inputs?")

person(h, i)

print("Variable length arguments")


def sum(m, *n): # The asterisk indicates a variable of unknown length
    print(m)
    print(n)
    p=m

    for i in n:
        p = p + i
    print(p)

sum(4,5,6,7,8,9,10)

print("Simpler Variable Length Arguements")

def sum3(*n): # The asterisk indicates a variable of unknown length
    print(n)
    p=0
    for i in n:
        p = p + i
    print(p)

sum3(4,5,6,7,8,9,10)