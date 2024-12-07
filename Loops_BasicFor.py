# Write your program here
daysInMonth = 30
daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
activities = ['work', 'yoga', 'study', 'sex', 'eat', 'hack']
x=3
y = 0
for i in range(1, daysInMonth+1):
    print(daysOfWeek[x], i, '\n  ', activities[y])
    x += 1
    y += 1
    if x > len(daysOfWeek)-1:
        x = 0
    if y > len(activities)-1:
        y = 0    