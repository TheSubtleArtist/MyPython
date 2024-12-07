'''
Modify the program we've created to include a second argument, which should be a word the program will always include. 
So if you specify a 3 word code name and provides the word "Blue" as a second argument, 1 of the 3 words should "Blue".

Create a rock-paper-scissors game you can play via the command line, using an argument to specify your move. 
Then have the program select a counter move at random, and proclaim a winner following the rules of rock-paper-scissors.

'''

import random
import sys

# Pick a random word from a provided list
def pick_random_word(list):
    return random.choice(list)

# Get a code name made up of the number of words specified
def get_code_name(list, num_words):
    if num_words.isdigit() == False:
        return 'Error: incorrect argument provided. You must provide an integer.'

    num_words = int(num_words)
    code_name = ''

    for x in range(1,num_words+1):
        word = pick_random_word(list)
        code_name += word + ' '

    return sys.argv[2] + ' ' + code_name.rstrip()

# List of words to use
word_list = ['Aurora', 'Avalanche', 'Blizzard', 'Cyclone', 'Eagle', 'Edison', 'Frost', 'Hawk', 'Hexagon', 'Hornet', 'Medusa', 'Neptune', 'Orion', 'Osprey', 'Plato', 'Portal', 'Raven', 'Sand', 'Shadow', 'Storm', 'Sunset', 'Thunder', 'Vector', 'Vista', 'Vortex', 'Volcano']


if __name__ == '__main__':
    if len(sys.argv) > 2:
        # Retrieve the command line argument
        words_to_pick = sys.argv[1]

        # Create a code name and print it to the screen
        code_name = get_code_name(word_list, sys.argv[1])
        print(code_name)
    else:
        print('Error: You must provide the number of words as an argument.')