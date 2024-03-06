#How and If / Else loop works.

nums = [12, 15, 18, 21, 26]

for num in nums:
    if num % 5 == 0:
        print(num)
    else:
        print ("not found")
print("next")
#How a For / Else loop works

bums = [12, 15, 18, 21, 26]
for num in bums:
    if num % 5 == 0:
        print(num)
        break
else:
    print ("not found")

print("next")
mums = [12, 16, 18, 21, 26]
for num in mums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")

    print("next")