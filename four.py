import sys

def number_to_word(n):
    """Convert single digit number to word."""
    words = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    return words[n]

def main():
    number = int(sys.argv[1])

    while number != 4:
        word = number_to_word(number)
        letter_count = len(word)
        print(f"The word {word} has {letter_count} letters in it.")
        number = letter_count

    print("The word four has 4 letters in it.")
    print("Done.")

if __name__ == "__main__":
    main()