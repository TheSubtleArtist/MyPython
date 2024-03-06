pos = -1
mynums = [2, 5, 9, 13, 16, 23, 45, 51, 59, 62, 64, 68, 71, 72, 78, 88, 99]
target = int(input("Enter a value"))

def search(data, val):
    lb = 0
    ub = len(data) - 1

    while lb <= ub:
        mv = (lb + ub) // 2

        if data[mv] == val:
            globals()['pos'] = mv
            return True
        elif data[mv] < val:
                lb = mv + 1
        elif data[mv] > val:
                ub = mv - 1
    return False







if search(mynums, target):
    print(target, "was found at position", pos + 1)
else:
    print(target, "not found")
