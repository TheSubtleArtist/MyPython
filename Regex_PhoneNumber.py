"""
Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7, 8, or 9.
Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.
Input Format
The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.

"""

import re
# a total of 10 digits
# [789] indicates the first of the 10 digits must be 7, 8, or 9
#\d{9} requires the following 9 digits must be any Unicode decimal digit
# $ indicates the 10 digits is the limit of the line / input

pattern = re.compile(r"""[789]\d{9}$""")
for i in range(int(input())):
    if pattern.match(input()):
        print("YES")
    else:
        print("NO")