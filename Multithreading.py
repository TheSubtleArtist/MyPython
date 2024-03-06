'''
A thread is the smallest unit that is scheduled in an operating system, which can perform multitask simultaneously.
When the task requires some time for execution python threads are used in this scenario.
Running several threads is similar to running several different programs concurrently, but with the following benefits
-Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.
-Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
A thread has a beginning, an execution sequence, and a conclusion.
A thread has an instruction pointer that keeps track of where within its context it is currently running.
-It can be pre-empted (interrupted)
-It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.
-The threading module provided with Python includes a simple-to-implement locking mechanism that allows you to synchronize threads.


# traditional use of 'main' thread
class hello:
    def run(self):
        for i in range(5):
            print("hello")


class hi:
    def run(self):
        for i in range(5):
            print("hi")

t1 = hello()
t2 = hi()

t1.run()
t2.run()
'''

from threading import *  #<-- Import the threading class
'''
class goodbye(Thread): #<-- Make the goodbye class into a sub class of threading class
    def run(self):
        for i in range(500):
            print("hello")


class seeya(Thread): #<-- Make the seeya class into a sub class of threading class
    def run(self):
        for i in range(500):
            print("hi")

t1 = goodbye()
t2 = seeya()
#Following calls run wild until there are collisions and then the output looks random
t1.start()   #<-- specific to the threading class and creates a thread for the t1, also internally calls the 'run' method
t2.start()   #<-- specific to the threading class and creates a thread for the t2, also internally calls the 'run' method
'''


from time import sleep  #<--Necessary to begin controlling the outputs
class coffee (Thread):
    def run(self):
        for i in range(25):
            print("coffee")
            sleep(.5)

class espresso(Thread):
    def run(self):
        for i in range(25):
            print("espresso")
            sleep(.5)

t1 = coffee()
t2 = espresso()

t1.start()
sleep(.25)
t2.start()

t1.join()
t2.join()
print("FRAPPUCCINO")