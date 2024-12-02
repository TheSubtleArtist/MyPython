import numpy as np

x = np.array([0, 1, 0, 1], np.uint8)
y = np.array([0, 0, 1, 1], np.uint8)

def showBitwise(array1, array2):
    print("array1: ", array1)
    print("array2: ", array2)
    print(np.bitwise_and(array1, array2))
    print(np.bitwise_or(array1, array2))
    print(np.bitwise_xor(array1, array2))
    print(np.bitwise_not(array1))

def showRandint():
    arrRandInt= np.random.randint(low=0,high=16,size=32)
    print("randint: ", arrRandInt)
    print("Median: ", np.median(arrRandInt))
    print("Average: ", np.average(arrRandInt))
    print("Mean: ", np.mean(arrRandInt))
    print("variance: ", np.var(arrRandInt))
    print("Histogram: ", np.histogram(arrRandInt))



if __name__ == '__main__':
    showBitwise(x, y)
    showRandint()
    