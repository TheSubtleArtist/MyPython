print("Python has an interesting feature called decorators to add functionality to an existing code.")

def div1(a,b):
    print(a/b)
    print("The answer indicates the arguments were not passed in the correct order")
    print("We know the result should have been 2")
div1(2,4)

def div2(a,b):
    if a<b:
        a,b = b,a
    print(a/b)
    print("we have achieved the expected result")
div2(2,4)


print("what happens when the function is in another file to which you only have access to and cannot or do not want to change the code?")
print("This is where we need Decorators")

def div4(a,b):
    print(a/b)

def smart_div (func):
    def inner(a,b):
        if a < b:
            a, b = b, a
            return func(a,b)
    return inner

div4 = smart_div(div4)
div4(2,4)

