# Stack has only one end, the left.

stack = []
stack.append('a')
print(stack)
stack.append('b')
stack.append('c')
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = Node

class Stack:
    
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        
    def __str__ (self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeping from an empty stack")
        return self.head.next.value
    
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value