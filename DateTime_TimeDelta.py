"""
When users post an update on social media,such as a URL, image, status update etc., other
users in their network are able to view this new post on their news feed.
Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
Since sometimes posts are published and viewed in different time zones, this can be confusing.
You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time a and time b.

Example Input:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
"""

# My Attempt

import datetime

frmtDate = '%a %d %b %Y %X %z'
""" 
Sets the format for the input of a date string. 
Request the format of the input to be knonwn and unchanging
Comes from the datetime class
"""


n = int(input())  #Number of time pairs
for i in range(n):
	dateA = input()
	dateB = datetime.datetime.strptime(dateA, frmtDate)
	print(dateB)

	dateC = input()
	dateD = datetime.datetime.strptime(dateC, frmtDate)
	print(dateD)

	dateDelta = abs(dateD - dateB)
	deltaSeconds = dateDelta.total_seconds()
	print(int(deltaSeconds))


#Even Better:

import datetime
frmtDate = '%a %d %b %Y %X %z'

if __name__ == '__main__':
    for i in range(int(input())):
        dateA = datetime.datetime.strptime(input(), frmtDate)
        dateB = datetime.datetime.strptime(input(), frmtDate)
        
        print(int(abs(dateB-dateA).total_seconds()))


# Just in case you need to get really confusing:

import datetime
frmtDate = '%a %d %b %Y %X %z'

if __name__ == '__main__':
    for i in range(int(input())):
        print(int(abs(datetime.datetime.strptime(input(), frmtDate)-datetime.datetime.strptime(input(), frmtDate)).total_seconds()))
        





