#Class is a design / blueprint
#Object is the implementation of an individual instance based on a class
#Also includes Telusco 50 on __init__


#First, define a class

class Computer:
#build in Attributes (variables) and methods (functions)

    def __init__(self, cpu, ram):
        # init is executed automatically and does not need to be called
        #Accepts attributes for each object using the class
        #self refers to the name of the object to which you want to assign the attributes
        print("in init")
        self.obcpu = cpu
        self.obram = ram
    def config(self):
        print("config is ", self.obcpu, self.obram)






#Create the object
comp1 = Computer('i5', 16)
comp2 = Computer('Ryzen 3', 96)
print(type(comp1))
print(type(comp2))

#Now access the methods of a class and apply to the object in one of a couple way
comp1.config()
Computer.config(comp1)
comp2.config()
Computer.config(comp2)



