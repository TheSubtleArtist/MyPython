from functools import reduce

nums =[25, 30, 15, 12, 15, 56, 95, 69]
print(nums)
print("Filter: returns an iterator were the items are filtered through a function to test if the item is accepted or not.")
def fnd_even(n):
    return n%2 == 0

evens = list(filter(fnd_even, nums))
#Filter requires two arguements: function, iterable list/set/dictionary/ or something
#List establishes that the returned values of the function are to be put into a list datatype

print("Even numbers are ", evens)


print("Now with a lambda functions")
evens2 = list(filter(lambda n : n%2==0, nums))
print("Even numbers with lambda are ", evens2)


print("Map and recursion")
#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
evens3 = nums

evens4 = list(map(lambda n : n*2, evens3))
#This is being done in recursion and lambda
#n represents the value to be returned and the element
#n*2 is hte function, which is a required argument for "map"
# evens three is the iterable
print(evens4)


print("Reduce: applies a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.")

sum = reduce (lambda a,b : a+b, nums)
print(sum)


