"""
.difference()

The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).

Task

Students of District College have a subscription to English and French newspapers. 
Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, 
and some have subscribed to both newspapers.

You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to only English newspapers.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those students.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains space separated roll numbers of those students.


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
    print(len(engishStu - frenchStu))