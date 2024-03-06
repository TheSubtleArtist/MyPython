"""
ABCXYZ company has up to 100 employees.

The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0-9).
It should only contain alphanumeric characters (a-z, A-Z, 0-9).
No character should repeat.
There must be exactly 10 characters in a valid UID.

Input Format:
The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format:
For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.
"""

import re

for i in range(int(input())):
    #inputs the UID and sorts
    uid = ''.join(sorted(input()))

    # using a "try" will stop the search at any sign of invalid UID
    try:
        # looks for exactly two capital letters
        assert re.search(r'[A-Z]{2}', uid)
        # loosk for exactly three digits 
        assert re.search(r'[0-9]{3}', uid)
        # Matches the start of the string (^), essentially attempting to prevent injection
        assert not re.search(r'[^a-zA-Z0-9]', uid)
        # prevents the same character from being immediately repeated: 5 5 is okay but not 55
        # since the UID was sorted, this will actually prevent ANY instance of repetition
        assert not re.search(r'(.)\1', uid)
        # UID must be 10 characters
        assert len(uid) == 10
    except:
        print('Invalid')
    else:
        print('Valid')