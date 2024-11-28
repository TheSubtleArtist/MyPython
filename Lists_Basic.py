#Lists are ordered, changeable, and allows duplicate


nums =[25, 30, 15, 12, 15, 56, 95, 69] # List requires the brackets
print("Entire List: ",nums)
print("Index 2: ", nums[2])
print("Index 4: ", nums[4:])
print("Index -2: ", nums[-2])
print("Slide ':6': ",nums[:6])
print("Slice ':-4': ", nums[:-4])

names = ['Jo', 'Bob', 'Square', 'Pants', 'Keen']
print("Index 4: ",names[4])

mixed = ['slum', 'dog', 4, 4.5, -10]
print("Mixed List: ",mixed)

print("Append a value")
# m = int(input("Provide a number: "))
nums.append(int(input("Provide a number: ")))
print("nums is now " + str(nums))

print("Remove an element")
print(nums)
n = int(input("Choose one of these numbers: "))
nums.remove(n)
print("nums no longer contains " + str(n))
print(nums)

print("Deleting Multiple Values")
del nums[3:]
print(nums)

print("Exending the List")
nums.extend([20, 25, 30, 35, 40, 45, 98, 42, 452,])
print("Extended: ", nums)

srtNums=nums.sort()
print("Sort: ", srtNums)
revNums=nums.sort(reverse=True)
print("Reverse: ", revNums)


#Mathematics
print("Min method: ",min(nums))
print("Max method: ", max(nums))
print("sum method: ", sum(nums))
