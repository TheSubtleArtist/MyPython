"""
Python has built-in string validation methods for basic data. 
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
The result of any test is true or false.
str.isalnum(): This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
str.isalpha(): This method checks if all the characters of a string are alphabetical (a-z and A-Z).
str.isdigit(): This method checks if all the characters of a string are digits (0-9).
str.islower(): This method checks if all the characters of a string are lowercase characters (a-z).
str.isupper(): This method checks if all the characters of a string are uppercase characters (A-Z).

Task

You are given a string 'myTestString'

Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""

myTestString="Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters."

def validateString(string):
    string.strip()
    stringList = list(string)
    print(any(str.isalnum() for str in stringList))
    print(any(str.isalpha() for str in stringList))
    print(any(str.isdigit() for str in stringList))
    print(any(str.islower() for str in stringList))
    print(any(str.isupper() for str in stringList))


if __name__ == '__main__':
    validateString(myTestString)