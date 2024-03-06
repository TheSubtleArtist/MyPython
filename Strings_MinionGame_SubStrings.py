'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, 'S'.
Both players have to make substrings using the letters of the string 'S'.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string 'S'.

For Example:
String 'S'  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.



Your task is to determine the winner of the game and their score.

Function Description

minion_game has the following parameters:

string string: the string to analyze

Prints string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

Input Format

A single line of input containing the string .
Note: The string 'S' will contain only uppercase letters:[A-Z] .

'''
from itertools import combinations

def minion_game(string):
    kevin_score_vowels = 0
    stuart_score_consonants = 0
    vowels_list = ['A', 'E', 'I', 'O', 'U'] # used to sort permutations between kevin and stuart

    for index, value in enumerate (string):
        if value in vowels_list:
            kevin_score_vowels += (len(range(index, len(string))))
        else:
            stuart_score_consonants += (len(range(index, len(string))))
    
    if kevin_score_vowels > stuart_score_consonants:
        print('Kevin', kevin_score_vowels)
    elif stuart_score_consonants > kevin_score_vowels:
        print('Stuart', stuart_score_consonants)
    else:
        print('Draw')
    


if __name__ == '__main__':
    s = 'BANANA' #input()
    minion_game(s)