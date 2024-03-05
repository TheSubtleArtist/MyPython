# Organizing a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Permanent Sort")
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print()
print()
print("Temporary Sort")
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print(f"The original list is\n{cars2}.")
print(f"\nThis is the sorted list:\n{sorted(cars2)}.")
print(f"\nThe original list is:\n{cars2}.\n\n")

print("Printing in Reverse Order.\n")
print(cars2)
cars2.reverse()
print(cars2)
print()
print("Finding the length of a list")
print(cars)
print(len(cars))
