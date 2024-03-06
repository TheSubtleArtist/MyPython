#This will find the minmimum value and move it.
#No need to set the index values to 0 because it will only be tru on the first iteration

#mynums = [5, 84, 89, 6, 89, 842, 9842, 96, 86]

mynums = [84, 65, 14, 89, 6, 156, 18, 541, 28, 9, 42, 5, 842, 9842, 96, 86]


def sort(data):
    for i in range(len(data)-1):
        minvalpos = i #captures the index value of the minimum value in the unsorted portion of mynums list
        for j in range(i, len(data)):
            if data[j] < data[minvalpos]:
                minvalpos = j


        temp = data[i]
        data[i] = data[minvalpos]
        data[minvalpos] = temp
        print(mynums)
sort(mynums)
print(mynums)