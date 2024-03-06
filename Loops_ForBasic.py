# Works on sequences like lists, tuples, and strings

x = ["Name", 60, 2.5]

# prints all the values in list x
for i in x:
    print(i)

y = "ThisIsMyName"
for i in y:
    print(i)


for i in range(0, 50, 5): #range(starting value, ending value, increment value)
    print(i)

for i in range(101, 502, 5): #range(starting value, ending value, increment value)
    if(i % 2 == 0):
        print(i)
    else:
        print("Oddly Enough")