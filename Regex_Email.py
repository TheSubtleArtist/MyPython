"""
A valid email address meets the following criteria:
-It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
-The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
-The domain and extension contain only English alphabetical characters.
-The extension is 1, 2, or 3 characters in length.

Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
Hint: Try using Email.utils() to complete this challenge. For example, this code: 

import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
produces this output:
('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>

Input Format

The first line contains a single integer, n , denoting the number of email address.
Each line i of the n subsequent lines contains a name and an email address as two space-separated values following this format:

name <user@email.com>
"""

import email.utils
import re
pattern = re.compile(r"""
#Begins with english letters
^[a-z][A-Z]
# matches a set of a variety of elements
# \w includes all englist letters and numbers as well as underscore
# \-. adds hyphen and period to the set of allowed characters
# * matches 0 or more characters from the preceding set
[\w\-.]*
# literal match
@
# english alphabetical characters for the domain name
# + requires the domain name be at least 1 character
[a-zA-Z]+
# literal match but the period requires an escape
\.
#the extension must be 1 to 3 characters
[a-zA-Z]{1,3}
# set end of line
$
""", re.VERBOSE)

for i in range(input()):
    uname, umail = email.utils.parseaddr(input())
    if pattern.match(umail):
        print(email.utils.formataddr((uname, umail)))