"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Input Format:
The first line contains an integer,N, the number of students.
The subsequent 2N lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade. 

Output Format:
Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line.
"""


from operator import itemgetter

records = {}
scores=[]
names=[]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score
        scores.append(score)
    scores = set(scores)
    scores = sorted(scores)
    tScore = scores[1]
    for key, value in records.items():
        if value == tScore:
            names.append(key)
    names.sort()
    for each in names:
        print(each)