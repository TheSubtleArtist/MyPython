# Tuple
# immutable

# Defining a Tuple

dimensions = (200, 50)  # Tuples require parenthesis
tuple1 = (
	3,)  # A tuple of one element, the comma defines the tuple more than the parentesis
print(dimensions[0])
print(dimensions[1])

# Writing over a Tuple

print("Original dimensions:")
for i in dimensions:
	print(i)

dimensions = (400, 150)  # re-initializing the tuple
print("\n Modified dimensions:")
for i in dimensions:
	print(i)
