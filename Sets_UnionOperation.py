"""
.union()

The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).

Task

The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

The first line contains an integer, the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those students.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains space separated roll numbers of those students. 

https://www.youtube.com/watch?v=RedXJ3HwK1c

"""
# this is unnecessary input
englishSub = input()

#necessary input
engishStu = set(map(int, input().split()))

#unnecessary input
frenchSub = input()

#necessary input
frenchStu = set(map(int, input().split()))

# creates the union
unionStu = engishStu | frenchStu

# for testing only, will get rejected if included in the answer
print(unionStu)

# the answer
print(len(unionStu))


# MOre advanced answer: 

if __name__ == '__main__':
    #unneccessary input
    e = input()
    #necessary input
    enStu = set(map(int, input().split()))
    # another unnecessary input
    f = input()
    frStu = set(map(int, input().split()))
    print(len(enStu | frStu))
