names = ['clara', 'amy', 'martha', 'jack', 'rose']
for i in range(len(names)):
	print(f"{names[i].title()}, please come to my party, and bring your accent.")

decline = 'jack'
names[3] = 'Donna'
print()
print(
	f"Bad news, {decline.title()} cannot make the party. We will invite {names[3].title()}, instead.")
print()
for i in range(len(names)):
	print(f"{names[i].title()}, please come to my party, and bring your accent.")
print()
for i in range(len(names)):
	print(
		f"{names[i].title()}, it seems we have found additional table space for our party.")
names.insert(0, 'rory')
names.insert(int(len(names) / 2), 'tegan')
names.append('sara jane')
print()
for i in range(len(names)):
	print(f"{names[i].title()}, please come to my party, and bring your accent.")
