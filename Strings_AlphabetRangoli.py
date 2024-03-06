"""
You are given an integer, N . 
Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
String Module
"""

import string

def print_rangoli(size):
  # create a place to store all the lower case letters
    letters = string.ascii_lowercase
    rList = []
    
    for i in range(size):
        # create a substring that holds all the letters that will be used
        line = '-'.join(letters[i:n])
        rList.append((line[::-1]+line[1:]).center(4*size-3, '-'))
    print('\n'.join(rList[:0:-1] + rList))    
    
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)