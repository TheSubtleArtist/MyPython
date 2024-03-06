#Lists are ordered, changeable, and allows duplicate


nums =[25, 30, 15, 12, 15, 56, 95, 69] # List requires the brackets
print(nums)
print(nums[2])
print(nums[4:])
print(nums[-2])
print(nums[:6])
print(nums[:-4])

names = ['Jo', 'Bob', 'Square', 'Pants', 'Keen']
print(names[4])

mixed = ['slum', 'dog', 4, 4.5, -10]
print(mixed)

print("Append a value")
m = int(input("Provide a number"))
nums.append(m)
print("nums is now " + str(nums))

print("Remove an element")
print(nums)
n = int(input("Choose one of these numbers"))
nums.remove(n)
print("nums no longer contains " + str(n))
print(nums)

print("Deleting Multiple Values")
del nums[3:]

print("Adding Multiple Values")
nums.extend([20, 25, 30, 35, 40, 45, 98, 42, 452,])
print(nums)

#Mathematics
min(nums)
max(nums)
sum(nums)
print(nums)
nums.sort()
print(nums)
