"""
You are given an HTML code snippet of N lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]

The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
All attributes have an attribute value.

Input Format

The first line contains an integer N, the number of lines in the HTML code snippet.
The next N lines contain HTML code.

"""

from html.parser import HTMLParser

start_tags = []
end_tags = []
tagsStartEnd = []
commentsList = []

class Parser(HTMLParser):
  
  # method to append the start tag to the list start_tags.
  def handle_starttag(self, tag, attrs):
    global start_tags
    start_tags.append(tag)
    print(tag)
    for elements in attrs:
        print('->', elements[0], '>', elements[1])
  
  # method to append the end tag to the list end_tags.
  #def handle_endtag(self, tag):
    #global end_tags
    #end_tags.append(tag)
    #print (tag)
  
  # method to append the data between the tags to the list all_data.
  #def handle_data(self, data):
      #if data.strip():
        #print(data)
  
  # method to append the comment to the list comments.
  #def handle_comment(self, data):
      #global commentsList
      #commentsList.append(data)
      #print('Comment:',data)
  
  # method to print empty tags
  def handle_startendtag(self, tag, attrs):
      global tagsStartEnd
      tagsStartEnd.append(tag)
      print(tag)
      for elements in attrs:
          print('->', elements[0], '>', elements[1])

# Creating an instance of our class.
parser = Parser()
# Poviding the input.

for i in range(int(input())):
    parser.feed(input())
