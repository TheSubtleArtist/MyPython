motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print()
motorcycles[0] = 'ducati'
print(motorcycles)
print()
motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)
motorcycles2 = []

for i in range(len(motorcycles)):
	motorcycles2.append(motorcycles[i])
print(motorcycles2)

motorcycles3 = ['honda', 'yamaha', 'suzuki']
print()
del motorcycles3[0]
print(motorcycles3)
print()

motorcycles3 = ['honda', 'yamaha', 'suzuki']
del motorcycles3[1]
print(motorcycles3)
print()

print("pop")
motorcycles4 = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles4.pop()
print(last_owned)
print(motorcycles4)
print(f"The last motorcycle I owned was a {last_owned.title()}")
print()
print("Remove")
motorcycles5 = ['honda', 'yamaha', 'suzuki', 'ducati']
expensive = 'ducati'
motorcycles5.remove(expensive)
print(motorcycles5)

# Reverse Slicing
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])
# print()
print(motorcycles[-1])


# Slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:2])  # indicates the start is "0" and stops at position 2
print(players[2:])  # indicates the start is "2" and proceeds to the end of the list
print(
	players[-3:])  # starts from the third element from the end and moves toward the end

# Loop through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

