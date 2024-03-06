"""
We have seen the applications of union, intersection, difference and symmetric difference operations, 
but these operations do not make any changes or mutations to the set.

We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

TASK
You are given a set A and N number of other sets. 
These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.

Input Format

The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2*N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
"""
# unnecessary input, number of elements in the original set
A = input()

# create original set
elementsA = set(map(int, input().split()))

# number of expected instructions
N = input()


for i in range(int(N)):
    # create list of instructions, but position [1] is never used
    instructions = list(input().split())

    #testing, remove before submitting
    print(instructions)

    # create set of elements as parameter to the instruction
    elements = set(map(int, input().split()))

    # testing, remove before submission
    print(elements)

    # execute the instructions previosly given. Notice the lack of any call to 'instructions[1]
    eval(f'elementsA.{instructions[0]}({elements})')

    # testing purpose
    print(elementsA)

# print the answer
print(sum(elementsA))