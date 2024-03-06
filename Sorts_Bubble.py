
#Each iteration requires multiple swaping, consuming unnecessary power and time


#mynums = [5, 84, 65, 14, 89, 6, 156, 18, 541, 28, 9, 42, 89, 842, 9842, 96, 86]

mynums = [5, 84, 65, 14, 89, 6, 156, 18, 541, 28, 9, 42, 89, 842, 9842, 96, 86]


def sort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range (i):
            if data[j]>data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j + 1] = temp

sort(mynums)
print(mynums)
