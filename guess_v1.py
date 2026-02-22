import random  # gives us tools for picking random numbers

secret = random.randint(1, 20)  # a <= secret <= b
tries = 0
guess = 0  # start with a value that cannot be the secret (since secret is 1..20)

print("I'm thinking of a number between 1 and 20")

text = input("Take a guess: ")  # input() returns text (a string)
guess = int(text)  # convert the text to a number

tries = tries + 1  # add 1 try
