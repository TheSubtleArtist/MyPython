"""
Let's learn some new Python concepts! 
You have to generate a list of the first N fibonacci numbers, 0 being the first number. 
Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Concept
The map() function applies a function to every member of an iterable and returns the result. 
It takes two parameters: first, the function that is to be applied and secondly, the iterables.
Let's say you are given a list of names, and you have to print a list that contains the length of each name. 

Lambda is a single expression anonymous function often used as an inline function. 
In simple words, it is a function that has only one line in its body. 
It proves very handy in functional and GUI programming. 

Note:
Lambda functions cannot use the return statement and can only have a single expression. 
Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself.
Lambda can be used inside lists and dictionaries. 

Recursion and Memoization

https://www.youtube.com/watch?v=Qk0zUZW-U_M

"""
"""
# implements recursion to calculate the sequence. But, becomes obnoxiously slower as the iterations progress
def fibonacciRecursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacciRecursion(n-1) + fibonacciRecursion(n-2)

for n in range(int(input())): 
    print(fibonacci(n))
"""
"""
def fibonacciMemoisation(n):
    # check the dictionary to see if the value has already been calculated
    if n in fibonacciDict:
        return fibonacciDict[n]
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        #calculate the next value in the fibonacci sequence
        value =  fibonacciMemoisation(n-1) + fibonacciMemoisation(n-2)
     #store the value in the dictioanry
    fibonacciDict[n] = value
    return value


# stores previous calculations to prevent delays due to extensive recursion
fibonacciDict = {}

for n in range(int(input())): 
    print(str(n+1) + ': ' + str(fibonacciMemoisation(n)))
"""

from functools import lru_cache

# by defaul lru_cache creates invisible dictionary to story values for the first 120 keys
# use lru_cache(x) to specify the dictionary store x number of values
@lru_cache
def fibonacciCache(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacciCache(n-1) + fibonacciCache(n-2)

cubed = lambda x: pow(x, 3)
    
fibs = []
for i in range(int(input())):
    fibs.append(cubed(fibonacciCache(i)))
print(fibs)
    

"""
# Website Solution
 cube = lambda x: pow(x,3)# complete the lambda function 
 def fibonacci(n):
     # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])

"""