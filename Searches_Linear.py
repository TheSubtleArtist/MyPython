#Linear Search

#Two Key Points
#-Element is in the list
#-Elementn is not in the list

num = int(input("Enter a whole number"))
pos=-1
list = [5, 84, 65, 14, 89, 6, 156, 18, 541, 28, 9, 42, 89, 842, 9842, 96, 86]
'''
def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False
'''

def search(list, n):
    i = 0
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False


if search(list, num):
    print(num, "has been found at position", pos+1)
else:
    print(num, "not found")

