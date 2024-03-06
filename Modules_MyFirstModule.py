#Since the _name_ variable has double underscores at both sides, it’s called dunder name. The dunder stands for double underscores
#It’s special because Python assigns a different value to it depending on how its containing script executes.



print(__name__)

import Modules_ImportMyFirstModule
print("The module was imported. The call to the __name__ within the module returns the module name, not __main__")
print(__name__)





def hello():
    print("Hello User")
    print("I have no idea what I'm doing")

'''
The following code is executed only when name is main. 
The following code will not be executed if this module is imported into another module
This is commonly used, for example, when executing a slash screen or welcome screen
'''
if __name__ == "__main__":
    hello()

