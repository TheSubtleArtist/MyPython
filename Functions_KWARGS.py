#Keyword Variable Length Arguements
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

#define the function
def person(name, **unknowndata):
    print(name)
    print(unknowndata)
    print("notice the printout inserts the colons to establish a keyword dictionary")
    print("printing via a different method")
    for i, j in unknowndata.items():
        print(i,j)


person('navin', age=28, city='Mumbai', mob=19995551212) #Call the function