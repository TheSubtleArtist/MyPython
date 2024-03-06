"""
HTML
Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

Parsing
Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.

HTMLParser
An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered. 

Task

You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately. 

Input Format

The first line contains integer N , the number of lines in a HTML code snippet.
The next N lines contain HTML code.

Output Format

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.
"""
from html.parser import HTMLParser

start_tags = []
end_tags = []
all_data = []
comments = []

class Parser(HTMLParser):
  
  # method to append the start tag to the list start_tags.
  def handle_starttag(self, tag, attrs):
    global start_tags
    start_tags.append(tag)
    print("Start :", tag)
    for elements in attrs:
        print('->', elements[0], '>', elements[1])
  
  # method to append the end tag to the list end_tags.
  def handle_endtag(self, tag):
    global end_tags
    end_tags.append(tag)
    print ("End  :", tag)
  
  # method to append the data between the tags to the list all_data.
  def handle_data(self, data):
    global all_data
    all_data.append(data)
  
  # method to append the comment to the list comments.
  def handle_comment(self, data):
    global comments
    comments.append(data)
  
  # method to print empty tags
  def handle_startendtag(self, tag, attrs):
      print("Empty :", tag)
      for elements in attrs:
          print('->', elements[0], '>', elements[1])

# Creating an instance of our class.
parser = Parser()
# Poviding the input.

for i in range(int(input())):
    parser.feed(input())
#print("start tags:", start_tags)
#print("end tags:", end_tags)
#print("data:", all_data)
#print("comments", comments)