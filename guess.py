from random import randint

breakpoint()

answer = randint(0, 1)
n = input("Guess: 0 or 1? ")

if n == answer:
    print("Correct!")
else:
    print(f"Incorrect. The answer was {answer}.")