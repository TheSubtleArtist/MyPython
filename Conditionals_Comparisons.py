# Numerical comparisons

age = 18
if age == 18:
	print("Match")
else:
	print("No Match")

answer = 17
if answer != 42:
	print("No Match")
else:
	print("Match")

age = 18
if age < 18:
	print("Age is less than 18")
else:
	print("Age is greater than 18")
if age > 18:
	print("Age is greater than 18")
else:
	print("Age is less than 18")
if age <= 18:
	print("Age might be under 18")
else:
	print("Age is greater than 18")
if age >= 18:
	print("Age might be greater than 18")
else:
	print("Age is less than 18")

# Using "AND" to check multiple Conditions

age0 = 22
age1 = 18

if age0 >= 21 and age1 >= 21:
	print("True")
else:
	print("False")

age1 = 22
if age0 >= 21 and age1 >= 21:
	print("True")
else:
	print("False")

# Improve Readability
age0 = 22
age1 = 18
if (age0 >= 21) and (age1 >= 21):
	print("True")
else:
	print("False")

age1 = 22
if (age0 >= 21) and (age1 >= 21):
	print("True")
else:
	print("False")

# Using "OR" to check multiple Conditions

age0 = 22
age1 = 18
if (age0 >= 21) or (age1 >= 21):
	print("True")
else:
	print("False")

age0 = 18
if (age0 >= 21) or (age1 >= 21):
	print("True")
else:
	print("False")
