import sys
from random import randint


def roll_dice(*nums):
    """Roll dice with the given number of sides and return the sum."""
    if not nums:
        nums = [6]
    return sum(randint(1, n) for n in nums)


def main():
    """Main function that parses command line arguments and rolls dice."""
    dice_sides = [int(n) for n in sys.argv[1:]]
    result = roll_dice(*dice_sides)
    print(result)


if __name__ == "__main__":
    main()