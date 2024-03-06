"""
You are given a string, and you have to validate whether it's a valid Roman numeral. 
If it is valid, print True. 
Otherwise, print False. 
Try to create a regular expression for a valid Roman numeral.

https://dev.to/alexdjulin/a-python-regex-to-validate-roman-numerals-2g99

Rules of roman numerals:
Roman numbers are ranging from [I] 1 to [MMMCMXCIX] 3999
Numerals should follow a precise order: [M] 1000 / [D] 500 / [C] 100 / [L] 50 / [X] 10 / [V] 5 / [I] 1
A numeral cannot repeat more than 3 times, it then uses a pair
The following pairs are allowed: [CM] 900 / [CD] 400 / [XC] 90 / [XL] 40 / [IX] 9 / [IV] 4
"""

import re



regex_pattern = re.compile(r"""
# Checks for 0-3 [M] at the start of the string, indicating the possibility the number is between 1000-3000
^M{0,3}
# One pair [CM] or one pair [CD] or [D]. Whatever of those appears may be followed by 0-3 instances of [C]. Each element is opitional [?], as well as the entire block [()?].
(CM|CD|D?C{0,3})?
# One pair [XC] or one pair [XL] or [L]. Whatever of those appears may be followed by 0-3 instances of [X]. Each element is opitional [?], as well as the entire block [()?].
(XC|XL|L?X{0,3})?
# One pair [IX] or one pair [IV] or [V]. Whatever of those appears may be followed by 0-3 instances of [I]. Each element is opitional [?], as well as the entire block [()?].
# Whatever appears should be at the end of the string [$].
(IX|IV|V?I{0,3})?$
# re.verbose allows this code to be separated onto multiple lines for clarity and easy reading
""", re.verbose)

if regex_pattern.match(input()):
    print("True")
else:
    print("False")

