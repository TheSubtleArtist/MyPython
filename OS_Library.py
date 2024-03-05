"""
This week we will create a program that performs file processing activities.
Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
The program should then prompt the user for their name, address, and phone number.
Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user.
Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes.
Submit a link to your Github repository.
"""

import os
from tkinter.filedialog import askdirectory


def writeUserInput():
	f = open(filepath, 'w')

	f.write(name + ', ' + street + ', ' + city + ', ' + state + ', ' + zip)
	f.close()


name = input("Enter your name")
street = input("Enter your street address")
city = input("Enter the city in which you live")
state = input("Enter the state")
zip = input("Enter the zip code.")
file = input("Enter a file name.")
file = file + '.txt'
directory = input("Enter the path of your file: ")
filepath = os.path.join(directory, file)

if os.path.exists(filepath):
	writeUserInput()
else:
	print('Your filepath did not work. Please attempt our other method.')
	path = askdirectory(title='Select Folder')  # shows dialog box and return the path
	filepath = os.path.join(path, file)
	writeUserInput()

print(path)
