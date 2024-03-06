#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:
#keys should be immutable, and may be any type

dict1 = {1:'navin', 2:'Kiran', 4:'Harsh'}
print(dict1)

print("calling the data requires calling the key")
print(dict1[4])

print("the 'get' function also works")
print(dict1.get(2))

print("when the index doesn't have a value")
print(dict1.get(3), 'Not Found')


# Separating Keys and Values
keys1 = ['a', 'b', 'c', 'd'] #notice the brackets, not the curly brackets
values1 = ['python', 'java', 'C++', 'javascript']
dict2 = dict(zip(keys1, values1))
print(dict2)
print(dict2.get('b'))

#Add to the dictionary is done by using a new index key and assigning a value to it

dict3 = dict2
print(dict3)
dict3['e'] = 'perl'
print(dict3)

#Remove from the dictionary is done by several items

#The pop() method removes the item with the specified key name:
dict4 = dict3
print(dict4)
dict4.pop ('e')
print(dict4)

#The popitem() method removes the last inserted item
dict5 = dict2
print(dict5)
dict5['e'] = 'perl'
print(dict5)
dict5.popitem()
print(dict5)

print("lots more methods available for dictionaries")

#Inserting lists and dictionaries inside of a dictionary
prog = {'js':'Atom', 'CS':'VS', 'Python':['Pycharm','Sublime'], 'Java':{'JSE':'Netbeans', 'Jee':'Eclipse'}}
print(prog)
print("Programming in Python is commonly done with " + str(prog.get('Python')) +".")