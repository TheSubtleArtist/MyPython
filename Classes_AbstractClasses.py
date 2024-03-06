'''
Abstract Classes are not supported in Python
Abstract Classes are a good practice of DRY (Don't Repeat Yoruself)
An abstract class defines a common interface for a set of subclasses.
It provides common attributes and methods for all subclasses to reduce code duplication.
It also enforces subclasses to implement abstract methods to avoid odd inconsistencies.
Makes most sense in object oriented programming
Abstract classes have no initiatiion, just a bund of declarations for be commonly used by lots of other classes
'''
from abc import ABC, abstractmethod  #<-- imports the Abstract Base Classes module

class Computer:   # <-- Class
    def process(self):  #<-- Method
        print("Running Computer Class")

    def process2(self): # <-- Abstract method has no declarations
        pass    # <-- Python's way of avoiding abstract is to use PASS to indicatre there are no genuine declarations


comp1 = Computer()
comp1.process() # <--- Not really abstract, but doesn't actually do anything.....


class Computer2(ABC):   # <-- Class that uses ABC as a Super Class
    @abstractmethod  #<-- tells the compiler it is working on an abstract class
    def process3(self, other):  #<-- Method
        print("Running2")

    def process4(self): # <-- Abstract method has no declarations
        pass    # <-- Python's way of avoiding abstract is to use PASS to indicatre there are no genuine declarations

#comp2 = Computer2() #<-- does not instantiate with abstract method
#comp2.process3


class Computer3(Computer2):   # <-- Class that uses Computer2, an abstract class,  as a Super Class
    pass

#comp3 = Computer3() #<-- does not instantiate with abstract method


class Programmer:
    def work(self, comp):
        print("Solving Bugs")
        comp1.process()



class WhiteBoard(Computer2):
    def write(self):
        print("Permanant Marker")
        print("In Black Ink")

Dale = Programmer()
Dale.work(comp1)

bigboard = WhiteBoard()
bigboard.write
