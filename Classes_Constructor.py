'''
Heap memory is a part of memory allocated to JVM, which is shared by all executing threads in the application.
It is the part of JVM in which all class instances and are allocated.
It is created on the Start-up process of JVM.
It does not need to be contiguous, and its size can be static or dynamic.
Space allocated to the memory is reclaimed through an automatic memory management process called garbage collection.
Every time the object is created, running the same code, a new memory space is created.
Heap memory is a shared area that is utilized during the runtime of Java applications.
It is created during the instantiation of Java Virtual Machine (JVM).
Memory Types:
stack: stores local variables
heap: dynamic memory for programmer to allocate
data: stores global variables, separated into initialized and uninitialized
text: stores the code being executed

'''


class Computer:
#build in Attributes (variables) and methods (functions)

    def __init__(self, cpu, ram, name):
        # init is executed automatically and does not need to be called
        #Accepts attributes for each object using the class
        #self refers to the name of the object to which you want to assign the attributes
        print("in init")
        self.obcpu = cpu
        self.obram = ram
        self.obnam = name
    def config(self):
        print("config is ", self.obcpu, self.obram, self.obnam)

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



