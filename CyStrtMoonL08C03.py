#
# There is a directory traversal vulnerability in the
# following page http://127.0.0.1:8082/humantechconfig?file=human.conf
# Write a script which will attempt various levels of directory
# traversal to find the right amount that will give access
# to the root directory. Inside will be a human.conf with the flag.
#
# Note: The script can timeout if this occurs try narrowing
# down your search
# Help 1: https://stackoverflow.com/questions/61068165/traverse-directory-at-url-to-root-in-python
# Help 2: https://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
# help 3: https://www.geeksforgeeks.org/directory-traversal-tools-in-python/
# Help 4: https://docs.python.org/3/library/urllib.request.html

import urllib.request
import os

cUrl = urllib.request.urlopen("http://127.0.0.1:8082/humantechconfig?file=human.conf")
cDir = "/tmp"

opener = urllib.request.FancyURLopener({})
with opener.open("http://www.python.org/") as f:
    f.read().decode('utf-8')

