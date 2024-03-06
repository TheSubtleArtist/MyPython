"""
You are given a valid XML document, and you have to print its score. 
The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has. 

The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

Output Format
Output a single line, the integer score of the given XML document.

Sample Input:

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output: 

5

Explanation:

The feed and subtitle tag have one attribute each - lang.
The title and updated tags have no attributes.
The link tag has three attributes - rel, type and href.

So, the total score is 1+1+3=5. 

There may be any level of nesting in the XML document. To learn about XML parsing, refer here.

NOTE: In order to parse and generate an XML element tree, use the following code:

>> import xml.etree.ElementTree as etree
>> tree = etree.ElementTree(etree.fromstring(xml))

Here, XML is the variable containing the string.
Also, to find the number of keys in a dictionary, use the len function:

>> dicti = {'0': 'This is zero', '1': 'This is one'}
>> print (len(dicti))



https://www.edureka.co/blog/python-xml-parser-tutorial/

Bottom line on this challenge, you are literally parsing enough information to count the number of "=" signs.

"""
'''
import sys
import xml.etree.ElementTree as etree

# Create a variable to store the string being input
xml = ''

# create for loop to handle the xml inputs
for i in range (int(input())):
    xml += input()

# convert / store the string as an actual tree
root = etree.fromstring(xml)

# for loop to count the number of attributes in the string
for i in root.iter():
    score = sum(len(i.attrib))

print(score)
'''


# Their Answer.....

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    return sum(len(child.attrib) for child in node.iter())

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))