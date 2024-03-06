#Print columns and rows
a = int(input("Enter the number of desired rows."))
b = int(input("Enter the number of desired columns."))

for i in range(a):
    for j in range(b): #notice the j. Python automatically understand a character after the word "for" indicates and index value
        print("# ", end="")
    print() #simply jumps to the next line

#Print a Triangle
c = int(input("Enter the number of desired rows."))


for i in range(c):
    for j in range(i + 1):
            #the "i" creates the number of colmns as "i" is incremented in the original for loop statement (line 14)
            #must have the "+1" because the starting point for a range index is always zero
        print("# ", end="")
    print() #simply jumps to the next line

#Print an upside down triangle
d = int(input("Enter the number of desired rows."))


for i in range(d):
    for j in range(d-i): #the "i" creates the number of colmns as "i" is incremented in the original for loop statement (line 14)
        print("# ", end="")
    print() #simply jumps to the next line