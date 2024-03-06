'''
Inner or Nested classes are not the most commonly used feature in Python.
The code is straightforward to organize when you use the inner or nested classes.
Grouping of two or more classes.
Suppose you have two classes Computer and CPU. Every Computer needs a CPU.
But, CPU won't be used without a Computer.
Make the CPU an inner class to the Computer. It helps save code.


'''


class Computer:
#build in Attributes (variables) and methods (functions)

    pwrbtn = 1 #This is a Class variable because it is created outside the init function

    #Create the inner class
    class CPU:
        def __init__(self, speed, socket, manufacturer):
            self.cpuspd = speed
            self.cpuskt = socket
            self.cpumkr = manufacturer
        def cpucfg(self):
            print("CPU Speed is ", self.cpuspd)
            print("CPU Socket is ", self.cpuskt)
            print("CPU Manufacturer is ",self.cpumkr)
    #Initialize and object of the class
    def __init__(self, screen, ram, name):
        '''
        init is executed automatically and does not need to be called
        Accepts attributes for each object using the class
        self refers to the name of the object to which you want to assign the attributes
        Creates INSTANCE Variables
        '''
        self.obscr = screen
        self.obram = ram
        self.obnam = name
        self.obcpu = self.CPU("1GHz", "L0", "fluffy")

    def cmpcfg(self):
        print("Screen size is ", self.obscr, " inches")
        print("RAM is ", self.obram)
        print("Name is ", self.obnam)
        print("This machine has ", self.pwrbtn, " power button.")



    def compare(self, other): #Accessor Method
        if self.obscr == other.obscr:
            print("The screen sizes are the same")
        else:
            print("The screen sizes are different")
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







#Create the objects

comp1 = Computer(17, 16, "Peeka")
comp1.cmpcfg()
proc1 = comp1.CPU("3GHz", "M5500", "AMD")
proc1.cpucfg()
print()
print()
comp2 = Computer(22, 64, "Chu")
comp2.cmpcfg()
proc2 = comp2.CPU("4.5GHz", "A6", "Intel")
proc2.cpucfg()





'''
print()
print("Computer 1")

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
comp1.cmpcfg()
Computer.cmpcfg(comp1)
comp2.cmpcfg()
Computer.cmpcfg(comp2)

#Comparing requires defining a new function
print("Comparing Objects (the computers).")
comp1.compare(comp1)
comp1.compare(comp2)

print("Accessing the Class Method")
print(comp1.ClsMtd())

print("Accessing the Static Method")
Computer.StcMtd()

