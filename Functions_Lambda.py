#Lambda = Functions without name
#You can pass any number of arguements, but must only use one expression


a = int(input("Please enter a number."))

'''def square(b): #This is a waste of space. Two lines for one expression
    return b*b

print(square(a))'''

b = lambda x : x * x

print(b(a))