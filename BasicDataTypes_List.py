"""
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
3. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

"""

list = []
if __name__ == '__main__':
    for N in range (int(input())):
        
        args = input().strip().split(' ')
        
        
        if args[0] == 'insert':
            list.insert(int(args[1]), int(args[2]))
            
        elif args[0] == 'print':
            print(list)
            
        elif args[0] == 'remove':
            list.remove(int(args[1]))
            
        elif args[0] == 'append':
            list.append(int(args[1]))
            
        elif args[0] == 'sort':
            list.sort()
            
        elif args[0] == 'pop':
            list.pop()
            
        elif args[0] == 'reverse':
            list.reverse()
        else:
            continue