"""
Variety of references:

https://www.python.org/dev/peps/pep-3101/
https://realpython.com/python-formatted-output/
"""


# Simple string formatting
def print_hi(name):
    print(f'Hi, {name}') 

# Slicing and formatting strings
def stringSlicing():
    print('{} {}'.format('one','two'))
    print('{1} {0}'.format('one','two')) # 0 and 1 are positional to the strings sent to the function
    print('{:>10}'.format('test')) #forces right justification of the string using 10 spaces
    print('{:10}'.format('test')) #prints the string 'test' using 10 spaces, leaving 6 spaces after the last letter
    print('{:_<10}'.format('test')) #left justified, 10 spaces, '_' as space filler
    print('{:_^10}'.format('test')) #center justified, 10 spaces, '_' as space filler
    print('{:_^9}'.format('test')) #center justified,  spaces, '_' as space filler, uneven distribution is placed to the right
    print('{:.5}'.format('crazylongwords')) #truncates to only the first 5 characters (the number following the period)
    print('{:10.5}'.format('crazylongwords')) #10 spaces, but only the first 5 characters"""

if __name__ == '__main__':
    print_hi(input("What is your name?"))
    stringSlicing()

