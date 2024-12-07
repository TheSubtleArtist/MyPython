import random
import sys

# Pick a random word from a provided list
def pick_random_word(list):
    return random.choice(list)

# Get a code name made up of the number of words specified
def get_code_name(list, num_words):
    code_name = ''

    for x in range(1,num_words+1):
        word = pick_random_word(list)
        code_name += word + ' '

    return code_name.rstrip()

# List of words to use
word_list = ['Aurora', 'Avalanche', 'Blizzard', 'Cyclone', 'Eagle', 'Edison', 'Frost', 'Hawk', 'Hexagon', 'Hornet', 'Medusa', 'Neptune', 'Orion', 'Osprey', 'Plato', 'Portal', 'Raven', 'Sand', 'Shadow', 'Storm', 'Sunset', 'Thunder', 'Vector', 'Vista', 'Vortex', 'Volcano']

# Create a code name and print it to the screen
code_name = get_code_name(word_list, 2)
print(code_name)