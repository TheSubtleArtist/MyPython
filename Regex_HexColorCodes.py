"""
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
Specifications of HEX Color Code

You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

Input Format

The first line contains N, the number of code lines.
The next N lines contains CSS Codes. 

CSS Code Pattern
"""

import re
# '#' begins all hex color codes
# ?: is non-capturing. This allows for a match based on the upcoming {3} but does not "consume" that match, therfore allowing the same match to be used as part of the following {1,2}
# [0-9a-fA-F] sets of possible values for hex color codes
# {3} indicates that the set must contain 3 chracters from the set
# {1,2} indicates there might be either 1 or 2 sets from the set. This is what causes the matching to accept either 3 or 6 characters as hex colors
# (?!\w) is a negative look ahead to rule out CSS selectors and cases like #1234
# (?=.*;) is a positive look ahead to make sure the line being checked ends in a semi-colon


pattern = re.compile(r"(#(?:[A-Fa-f0-9]{3}){1,2})(?!\w)(?=.*;)")

for i in range(int(input())):
    matches = re.findall(pattern, input())
    for m in matches:
        print(m)