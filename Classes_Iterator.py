'''
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
'''


nums = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #<--List
'''
it = iter(nums) #<-- converts the list "nums" into an iterator that will return one value at a time
print(it) # <-- actually prints the object address and no values

print(it.__next__()) # <-- fetches the next value of "i" and remembers the state of "i" from the last time called
print(it.__next__()) # <-- fetches the next value of "i" and remembers the state of "i" from the last time called
print(next(it)) # <-- fetches the next value of "i" and remembers the state of "i" from the last time called

for i in nums:
    print(i) # <-- prints all the values
'''

# Creating a custom iterator
class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self): # <--required because built-in methods are not available inside local classess and must be initialized inside the local / custom classes.
        return self
    def __next__(self): # <--required because built-in methods are not available inside local classess and must be initialized inside the local / custom classes.
        if self.num<=10:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration # <-- tells the if loop to stop once "val" exceeds the definition of the if loop

values = TopTen()

print(next(values)) #<-- no results because the class and the next / iter functions preven the duplication
for i in values:
    print(i)

