"""
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

The first line contains N and X separated by a space.
The next X lines contains the space separated marks obtained by students in a particular subject. 

Python’s zip() function creates an iterator that will aggregate elements from two or more iterables. 
You can use the resulting iterator to quickly and consistently solve common programming problems, like creating dictionaries. 

Task:
The National University conducts an examination of N students in X subjects.
Comput the average scores of each student

Input:
The first line contains N and X, separated by a space
The next X lines contains the space separated marks obtained by students in a particular subject.

https://www.youtube.com/watch?v=Kn6GRtiY4eM

"""

# create the list for collecting scores
thisData = []

# respective values for numbers of students and exams
numStudents, numSubjects = map(int, input().split())

for i in range(numSubjects):
    # input each line of exam scores and store in the designated set
    thisData.append(list(map(float, input().split())))

    #for testing and observation ohly
    print(thisData)

# initiate the zip to turn the whole thing on its side for the average function
for x in zip(*thisData):
    print("%0.1f"%(sum(x)/len(x)))