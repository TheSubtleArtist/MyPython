from numpy import *

arr = array([1, 2, 3, 4, 5])
print(arr)

arr1 = arr + 5
print(arr1)

arr2 = array([10, 11, 12, 13, 14])
arr3 = arr + arr2
print(arr3)

print("Mathematical functions")
print(sin(arr3))
print(sum(arr3))
print(min(arr3))

print("Concatenate")
print(concatenate([arr, arr2, arr3]))

print(" Duplicate an array, in memory this only creates two pointers to the same data location, not two different arrays")

arr4 = arr2
print(arr2)
print(id(arr2))
print(arr4)
print(id(arr4))

print("Creating two actually different arrays of the same values.")
arr5 = arr2.view()
print(arr2)
print(id(arr2))
print(arr5)
print(id(arr5))

print("What happens when you change the value in the first array you copied to make the second array")
arr2[2]=7
print(arr2)
print(id(arr2))
print(arr5)
print(id(arr5))
print("Notice the value in the destination array changed to match the value in the source array. This is shadow copy.")

print("Deep Copy creates the second array but breaks the shadow link")
arr6 = arr3.copy()
print(arr3)
print(id(arr3))
print(arr6)
print(id(arr6))
print("change the value of arr6[3] to 4")
arr6[3] = 4
print(arr3)
print(id(arr3))
print(arr6)
print(id(arr6))







