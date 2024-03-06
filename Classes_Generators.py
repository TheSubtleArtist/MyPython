'''
There is a lot of work in building an iterator in Python.
-implement a class with __iter__() and __next__() method, keep track of internal states, and raise StopIteration when there are no values to be returned.
-This is both lengthy and counterintuitive.

Python generators are a simple way of creating iterators.
-All the work we mentioned above are automatically handled by generators in Python.
-Agenerator is a function that returns an object (iterator) which we can iterate over (one value at a time).
-Generator is useful for getting large amounts of data, but only one value at a time.... like retrieving large amounts of data from a database


def topten():

    yield 1   # <-- "yield" turns a function into a generator
    yield 2
    yield 3
    yield 4
    yield 5

values = topten()  # <--Turns "values" into an array because "topten" uses "()" and not "[]"
#print(values.__next__())

#Now use the generator in a for loop

for i in values:
    print(i)

'''

def topten2():
    n = 1    # <-- acts as the index
    while n <= 10:
        sq = n*n
        yield sq # <-- "yield" turns a function into a generator
        n += 1



values2 = topten2()

for i in values2:
    print(i) # <-- uses the index "i" as representative of index "n" to print the value "sq"