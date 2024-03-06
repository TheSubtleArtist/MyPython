"""
.intersection()

The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).

Task

The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to both newspapers.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those students.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains space separated roll numbers of those students.

https://www.youtube.com/watch?v=Gb8zMt6gl-c
"""




if __name__ == '__main__':
    # this is unnecessary input
    englishSub = input()

    #necessary input
    engishStu = set(map(int, input().split()))

    #unnecessary input
    frenchSub = input()

    #necessary input
    frenchStu = set(map(int, input().split()))

    # Answer 
    print(len(engishStu & frenchStu))


