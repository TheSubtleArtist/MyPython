#Arrays require all the values to be of the same type. However, Arrays can change size

#import all array capabilities
from array import *


vals = array('i', [5, 9, -8, 4, 2] )

def showReverse(testArramy):
    print("vals typecode: ",vals.typecode)
    print("Position 1 as created: ",vals[1])
    vals.reverse()
    print("Position 1 after the 'reverse' function: ", vals[1])

def arrayLength(array):
    print ("array length: ", len(array))
    

def printWithRange(array):
    print ("i: ", end=" ")
    for i in range(len(array)):
        print(array[i], end=" ")

def accessWithIn(array):
    print("e: ", end=" ")
    for e in array:
        print(e, end=" ")


if __name__ == '__main__':

    #create an array.
    #First argument establishes the type of values to be stored in the array. "i" represents signed integers
    vals=array('i', [5, 9, -8, 4, 2] )

    showReverse(vals)
    arrayLength(vals)
    printWithRange(vals)
    accessWithIn(vals)
    # Clone an Array
    newVals = array(vals.typecode, (a for a in vals))
    accessWithIn(newVals)
    # Simultaenously clone and perform a transofrmation
    powVals = array(vals.typecode, (b*b for b in vals))
    accessWithIn(powVals)

