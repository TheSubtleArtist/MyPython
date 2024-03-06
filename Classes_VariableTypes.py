'''
 Member variables:
 Variables associated with a class.
 Two types of member variables are Class and Instance

Class variables:
These are also known as static member variables and there's only one copy of that variable that is shared with all instances of that class.
If changes are made to that variable, all other instances will see the effect of the changes.

Instance variables:
These variables belong to the instance of a class, thus an object.
Every instance of that class (object) has it's own copy of that variable.
Changes made to the variable don't reflect in other instances of that class.


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

    def compare(self, other):
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
comp1.compare(comp1)
comp1.compare(comp2)