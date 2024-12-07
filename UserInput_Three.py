'''
Create a rock-paper-scissors game you can play via the command line, using an argument to specify your move. 
Then have the program select a counter move at random, and proclaim a winner following the rules of rock-paper-scissors.


'''

import random
import sys

word_list = ['Rock', 'Paper', 'Scissors']

# Pick a random word from a provided list
def pick_random_word(list):
    return random.choice(list)

def rock(autoMove):
    if autoMove == 'paper':
        return 'Machine Wins!'
    else:
        return 'You Win!'

def paper(autoMove):
     if autoMove == 'scissors':
        return 'Machine Wins!'
     else:
        return 'You Win!'   

def scissors(autoMove):
     if autoMove == 'rock':
        return 'Machine Wins!'
     else:
        return 'You Win!' 

def findWinner(myMove):
    autoMove = pick_random_word(word_list).upper()
    print(autoMove)
    if myMove == 'rock':
        return rock(autoMove)
    elif myMove == 'paper':
        return paper(autoMove)
    else: 
        return scissors(autoMove)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Retrieve the command line argument
        myMove = sys.argv[1].lower()
        print(findWinner(myMove))
        
