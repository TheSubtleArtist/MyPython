"""
Task

You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer N, the number of elements in the set s.
The second line contains n space separated elements of set s. 
All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.
"""


if __name__ == '__main__':
    n = int(input()) # first line
    s = set(map(int, input().split())) # creates the set of number from input line 2
    for i in range(int(input())): # establishes the loop based on inputs of line threee
        eval('s.{0}({1})'.format(*input().split()+[' ']))
    print(sum(s))   






