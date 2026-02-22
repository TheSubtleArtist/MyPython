import random  # gives us tools for picking random numbers

# ----------------------------
# Guess the Number (Beginner Demo)
# ----------------------------
# The computer picks a secret number.
# The player keeps guessing until they find it.

MIN_NUMBER = 1
MAX_NUMBER = 20

secret = random.randint(MIN_NUMBER, MAX_NUMBER)  # a <= secret <= b
tries = 0
guess = 0  # start with a value that cannot be the secret (since secret is 1..20)

print("I'm thinking of a number between", MIN_NUMBER, "and", MAX_NUMBER)

# Repeat until the user guesses the secret number.
while guess != secret:
    text = input("Take a guess: ")  # input() returns text (a string)

    # If the user didn't type digits, we avoid crashing and ask again.
    if not text.isdigit():  # True only if all characters are digits
        print("Please type a whole number (like 7).")
    else:
        guess = int(text)  # convert the text to a number
        tries = tries + 1  # add 1 try (written long-form for clarity)

        # Give a hint using if / elif / else.
        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print("That number is out of range. Try again.")
        elif guess < secret:
            print("Too low, try again.")
        elif guess > secret:
            print("Too high, try again.")
        else:
            print("You got it in", tries, "tries!")
