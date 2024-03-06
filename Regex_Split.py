"""
You are given a string S consisting only of digits 0-9, commas, and dots.
Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in S.
It’s guaranteed that every comma and every dot in S is preceeded and followed by a digit.

https://docs.python.org/3/library/re.html
https://www.w3schools.com/python/python_regex.asp


"""
import re

# python comprehension works from the inside out

# re.split has two arguements (pattern, string)

# r'[.,]+' is the pattern and input() is the string
# if stdin = 1,000,000 the output of re.split(r'[.,]+', input()) is a three element list: ['1', '000', '000]
#
# The filter(function, iterable) function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
# 'None' as the first function will eliminate things that do not fit the criterial. in this case, it will eliminate negative signs or other symbols passing values we are looking for.
# the iterable is created by the re.split() function
# the * unpacks the iterable and sends each element to the "print" function
# since print() is called with a carriage return separator, all true elements of the iterable are printed on new lines.


if __name__ == '__main__':
     inNum = input()
     splitNum = re.split('[.,]', inNum)
     print(each for each in splitNum)



# Comprehension
print(*filter(None, re.split(r'[.,]+', input())), sep='\n')

