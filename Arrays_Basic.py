#Arrays require all the values to be of the same type. However, Arrays can change size

#import all array capabilities
from array import *


#create an array.

vals=array('i', [5, 9, -8, 4, 2] )
#First argument establishes the type of values to be stored in the array. "i" represents signed integers

print(vals.typecode)
print(vals[1])
vals.reverse()
print(vals[1])


vals_len = len(vals)
for i in range(vals_len):
    print(vals[i])

#second method to access the length of the array
for i in range(len(vals)):
    print(vals[i])

#Simplest Third method for calling the length

for e in vals:
    print(e)

#create a new array with the same values
newVals = array(vals.typecode, (a for a in vals))

for d in newVals:
    print(d)


#create a new array while performing a function on the values of the original array
powVals = array(vals.typecode, (b*b for b in vals))

for c in powVals:
    for i in vals:
        print(i, end = " ")
    print(c, end = " " )
