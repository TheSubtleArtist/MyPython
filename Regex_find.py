"""

re.findall()
The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings. 

re.finditer()
The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. 

Task
You are given a string S.
It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.

"""

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
S = input()


 
# 'r' means the the following is a "raw string", ie. backslash characters are treated literally instead of signifying special treatment of the following character.
# The question mark symbol ? matches zero or one occurrence of the pattern left to it.
# (?<=) matches if the current position in the string is preceded by a match for / that ends at the current position. This is called "positive lookbehind assertion". (?<=abc)def will find a match in abcdef, since the lookbehind will back up 3 characters and check if the contained pattern matches.
#  [%s] is roughly equivalent to  [\S] Matches any character which is not a whitespace character.
# [%s]{2,} looks for matches of 2 or more non-whitespace characters in a row. this is where the evaluation looks for a set of two vowels between two sets of two consonants.
# % (c, v, c) establishes the order 
# flags = re.I instructs the evaluation to ignore the case

m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))