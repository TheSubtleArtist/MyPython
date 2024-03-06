
def update(x):
    print(id(x))
    x=8
    print("x=" + str(x))

a = input("Please enter a character")
print(id(a))
print("Notice the addresses of the two variables is the same. This is pass by reference")
print("Now, notice the values of the two variables are still difference")
print("Pass by value passed the value assigned to the variable, but does not pass the address of the value. The value gets a different memory address")
print("Pass by reference passes the address of the value, not the value itself.This happens when you pass an OBJECT to a function.")
update(a)
print("a=" +str(a))
#Notice that x and a have the same address, even though their values are different
#When you pass a value into a function, the value and the variable will have the same address
print("Unlike other languages, Python does not use either pass by reference or pass by value")


def update(lst):
    print(id(lst))
    lst[1] = 69
    print("lst=" + str(lst))

lst = [10, 20, 30]
print(id(lst))
update(lst)
print("Updated List" + str(lst))