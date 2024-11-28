# FIFO Data Structure
# One end for entry, one end for exit

from queue import Queue

q = Queue(maxsize=3)
q.qsize()
q.put('a')
q.put('b')
q.put('c')

print(q)

print(q.full) # results in "true"

print(q.get()) # output: a
print(q.get()) # output: b
print(q.get()) # output: c

print(q.empty()) # result: true

q.put(1)
print(q.full()) # result: false because the max size is 3
print(q.empty()) # result: false because there is at least one element in the queue
