'''
Instance Methods:
This method can only be called if the class has been instantiated.
Once an object of that class has been created, the instance method can be called and can access all the attributes of that class.
An instance method is capable of creating, getting, and setting new instance attributes and calling other instance, class, and static methods

Accessor Method:
This method is used to access the state of the object i.e, the data hidden in the object can be accessed from this method.
This method cannot change the state of the object, it can only access the data hidden.
We can name these methods with the word get.

Mutator Method:
This method is used to mutate/modify the state of an object i.e, it alters the hidden value of the data variable.
It can set the value of a variable instantly to a new value.
This method is also called as update method.
We can name these methods with the word set.

Class Methods:
Methods have to be created with the decorator @classmethod,
These methods share a characteristic with the static methods in that they can be called without having an instance of the class.
The difference relies on the capability to access other methods and class attributes but no instance attributes.

Static Methods:
A static method in python must be created by decorating it with @staticmethod in order to let python now that the method should be static.
They can be called without instantiating the class.
These methods are self-contained, meaning that they cannot access any other attribute or call any other method within that class



'''


class Computer:
#build in Attributes (variables) and methods (functions)

    pwrbtn = 1 #This is a Class variable because it is created outside the init function

    def __init__(self, cpu, ram, name):
        # init is executed automatically and does not need to be called
        #Accepts attributes for each object using the class
        #self refers to the name of the object to which you want to assign the attributes
        #Creates INSTANCE Variables
        print("in init")
        self.obcpu = cpu
        self.obram = ram
        self.obnam = name
    def config(self):
        print("config is ", self.obcpu, self.obram, self.obnam, self.pwrbtn)

    def compare(self, other): #Accessor Method
        if self.obcpu == other.obcpu:
            print("The computer cpu are the same")
        else:
            print("The computer cpu are different")
        if self.obram == other.obram:
            print("The computer ram are the same")
        else:
            print("The computer ram are different")
        if self.obnam == other.obnam:
            print("The computer names are the same. Are you sure you are comparing two different computers?")
        else:
            print("The computer names are different")
        print()
    @classmethod #This is placed just prior to the definition of the class method
    def ClsMtd(cls):
        '''This is a Class Method
        Use of the class method requires the use of cls
        '''
        return cls.pwrbtn
        print()
    @staticmethod
    def StcMtd():
        '''
        Can be used to perform any action which does not modify or access any attribute of the class
        Simply performs needed activities, calculations, or anything else
        '''

        print("This is a static method")







#Create the object
print()
print("Computer 1")
comp1 = Computer('i5', 16, "Peeka")
print(type(comp1))
print(id(comp1))
print()
print("Computer 2")
comp2 = Computer('Ryzen 3', 96, "Choo")
print(type(comp2))
print(id(comp2))

print()
print()

#Now access the methods of a class and apply to the object in one of a couple way
print("Accessing the objects can be done in two different calls:")
comp1.config()
Computer.config(comp1)
comp2.config()
Computer.config(comp2)

#Comparing requires defining a new function
print("Comparing Objects (the computers).")
comp1.compare(comp1)
comp1.compare(comp2)

print("Accessing the Class Method")
print(comp1.ClsMtd())

print("Accessing the Static Method")
Computer.StcMtd()