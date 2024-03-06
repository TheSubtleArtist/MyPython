"""
.symmetric_difference()

The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).

Task
Students of District College have subscriptions to English and French newspapers. 
Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

https://www.youtube.com/watch?v=0Ug0BbVHuTk

"""


if __name__ == '__main__':

    # this is unnecessary input
    eSub = input()

    #necessary input
    eStu = set(map(int, input().split()))

    #unnecessary input
    fSub = input()

    #necessary input
    fStu = set(map(int, input().split()))

    # creates the symmetric difference
    #print(*sorted(eStu ^ fStu), sep='\n')

    print(len(eStu ^ fStu))