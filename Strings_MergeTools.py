"""
Conisider:
- A string, S of length N where S= C sub 0 C sub 1 ... C sub n-1
- An integer, K, where K is a factor of N

We can split S into (S/K)  substrings, where each substring, T sub i, consists of a continguious block of K characters in S.
Then, use each T sub i to create string U sub i such thaht
-The characters in U sub i are a subsequence of the characters in T sub i.
-Any repeat occurrence of a character is removed from the string such that each character in U sub i occurs exactly once.
In other words, if the character at some index J in T sub i occurs at a previous index < J in T sub i, then do not include the character in string U sub i.

Given S and K, print (N/K) lines where each line i denotes string U sub i.

"""

import textwrap
def merge_the_tools(string, k):
    # string is the given element to analyze
    # k is the directed size of substrings
    
    # Break string into elements of size k
    subStr = textwrap.wrap(string, k)
    
    # Eliminate duplicates in each element of subStr and print
    for each in subStr:
        each = list(dict.fromkeys(each))
        print(''.join(each))
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)