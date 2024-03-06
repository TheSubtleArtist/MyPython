import numpy

#Create a multi-dimensional array

arr1 = array([
            [1, 2, 3,7, 8, 9],
             [4, 5, 6, 10, 11, 12]
])

print(arr1.dtype)
print(arr1.ndim) #prints the number of dimensions in the array
print(arr1.shape) #prints the number of rows and columns
print(arr1.size) #prints the size of the entire block


arr2 = arr1.flatten() #flattens the multi-dimensional array into a single dimensional array
print(arr2)

arr3 = arr2.reshape(4, 3) #converts single dimensional array into a multimensional array. Arguments include number of (rows, Columns)
print(arr3)

arr4 = arr2.reshape(6, 2, 1) #Transforms an array into a multi-dimensional array (X, Y, Z) with X sub-arrays, each sub array having Y single dimensions arrays, and each single dimensiona array having Z elements
print(arr4)

#MATRICES


arr5 = array([
            [1, 2, 3, 7],
             [4, 5, 6, 10]
])

m=matrix(arr5)
print(m) # output loos the same as original array, but enables many more additional math functions

#Sometimes need to create a matrix based on input from another source, not internal
n=matrix('1 2 3 6 ; 4 5 6 7') #semicolon creates the second matrix array
print(n)

o=matrix('1 2; 3 6 ; 4 5; 6 7') #semicolon creates the second matrix array
print(o)

#Diagonal Elements
p=matrix('1 2 4 12; 3 6 10 13; 4 5 15 18; 6 7 21 22') #semicolon creates successive matrix arrays
print(diagonal(p))

#Basics of multiplying matrices
r = matrix('1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 16')
s = matrix('1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 16')
t = r + s
u = r * s # This does not work Telusco has another video
#Learn to multiply matrix at https://www.youtube.com/watch?v=BtDPVc7H1Zs
print(t)
print(u)





