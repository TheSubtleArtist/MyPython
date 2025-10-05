# Type() function displays the type of object being examined
number_Empty_Lines = 2
print('\n' * int(number_Empty_Lines))
answer = 42
user_input = "42"
print(type(answer))
print('\n' * int(number_Empty_Lines))
print(type(user_input))

# dir() lists attributes and methods available for manipulating and object
numbers = {2, 1, 3, 4, 7}
print(dir(numbers))
print('\n' * int(number_Empty_Lines))

# Filter for only "public" methods, meaning no double underscores

print([method for method in dir(numbers) if not method.startswith('_')])

print('\n' * int(number_Empty_Lines))
# View the variables in the current namespace as a method to start debugging
print(vars())

print('\n' * int(number_Empty_Lines))
from datetime import datetime

# REPR Return a string containing a printable representation of an object.
now = datetime.now()
print('\n' * int(number_Empty_Lines))
print(now)
print('\n' * int(number_Empty_Lines))
print(repr(now))

# help() provides documentation for any object
print('\n' * int(number_Empty_Lines))
print(help(str.split))