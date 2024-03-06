"""
If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps in her collection. She asked for your help. 
You pick the stamps one by one from a stack of country stamps.

Output the total number of DISTINCT country stamps on a single line.

"""
cntry = set()
if __name__ == '__main__':
    for i in range(int(input())):
        cntry.add(input().upper())
    print(len(cntry))
        