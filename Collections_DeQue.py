"""
"Double Ended Que"
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same
performance in either direction.

Task

Perform append, pop, popleft and appendleft methods on an empty deque d.
functions as list, but allows methods to the left of the list.

Input Format:
The first line contains an integer N, the number of operations.
The next  N lines contains the space separated names of methods and their values.

Output Format:
Print the space separated elements of deque d.

https://www.youtube.com/watch?v=m3JgSV1Obn8
"""

from collections import deque
d=deque('')
if __name__ == '__main__':
    for i in range (int(input())):
        eval('d.{0}({1})'.format(*input().split()+[' ']))
    print(*d)


