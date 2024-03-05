current_users = ['Clara', 'Amy', 'Martha', 'jack', 'rose', 'ADMIN']
new_users = ['ed', 'dave', 'martha', 'bob', 'cherry', 'admin']
templ = []

for name in current_users:
	temp = name.lower()
	templ.append(temp)
	print(templ)
current_users = templ[:]
print(current_users)

for names in new_users:
	if names in current_users:
		print(f"{names.title()} is already used. Please select a new username.")
	else:
		print(f"{names.title()} is available.")
