"""
A group() expression returns one or more subgroups of the match. 

A groups() expression returns a tuple containing all the subgroups of the match.

A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name. 

re.match(pattern, string, flags=0)
    If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object. Return None if the string does not match the pattern; note that this is different from a zero-length match.


Task
You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in (read from left to right) that has consecutive repetitions. 

https://realpython.com/regex-python/

"""

import re



#re.search(pattern, string) checks for a match anywhere in the string
# receive the input and strip any leading or trailing space characters
# [a-zA-Z0-9] is the pattern the accepts only alphanumeric characters
# \1 instructs to match the object just identified. This is what creates the "first repeated". Presumably if it were \2, it would look for three consecutive occurrances

S = re.search(r'([a-zA-Z0-9])\1+', input().strip())

# .group() Returns a tuple containing all the captured groups from a regex match. If you gave five strings maybe only three meet the pattern.
# inserting .groups(2) only returns the second group that matched the pattern
print(S.group(1) if S else -1)