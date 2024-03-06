f = open("Telusco65_Data.txt", 'r')
#f becomes the object
#open requires a minimum of two arguements, the file and the mode

print(f) #Prints about the file, but not the contents
#print(f.read()) #prints the entirety of the contents
#print(f.readline(15)) #Prints line 15

#readline uses a pointed that remembers its position
print(f.readline())
print(f.readline())
print(f.readline(), end=" ")
print(f.readline(), end=" ")
f.close()

g = open("Telusco65Data2.txt", 'w') #creates the file and prepares it for writing
g.write("WriteFirstLine ")
g.write("WriteSecondLine ")
g.close()
'''
g = open("Telusco65Data2.txt", 'w') #This call to the file will overwrite the previous. 
g.write("Darkside ") 
g.close()'''

g = open("Telusco65Data2.txt", 'a') #opens the file in append mode
g.write("Something Something Darkside ")
g.close()

f = open("Telusco65_Data.txt", 'r')
g = open("Telusco65Data2.txt", 'a') #opens the file in append mode
for data in f:
    g.write(data)
f.close()
g.close()

h = open('cintaku.jpg', 'rb') #since images are composed of numbers, we use "read binary" to access the file
j = open('cintakucopy.jpg', 'wb')  # writing to an image, or other number based file, use "write binary"
for i in h:
    j.write(i)
h.close()
j.close()