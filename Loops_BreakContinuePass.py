import random

def DemonstrateBreak (choice, myList):
    # Break identifies a value and exits the loop or function
    print(myList)
    for each in myList:
        print(each)
        if each == choice:
            print(f"Found Your Number: {choice}.")
            print("Breaking")
            break    
    print("Returning")

def DemonstrateContinue (choice, myList):
    # Continue idenfies a value does somethning with it and continues with the funciton or loop
    print(myList)
    for each in myList:
        if each == choice:
            print(f"Found Your Number: {choice}.")
            print("Continuing")
            continue
        print(each)     
    print("Complete")

def DemonstrateWithShuffle(choice, myList):
    random.shuffle(myList)
    DemonstrateBreak (choice, myList)
    DemonstrateContinue(choice, myList)
10
if __name__ == '__main__':
    n = int(input("Pick a number between 1 and 10:  "))
    nums=list(range(1,11))
    DemonstrateBreak(n, nums)
    DemonstrateContinue(n, nums)
    DemonstrateWithShuffle(n, nums)

