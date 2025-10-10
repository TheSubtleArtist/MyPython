from math import ceil, floor

def percent_to_grade(percent, *, suffix=False, round=False):
    if round:
        percent = round_half_up(percent)
    if percent >= 90:
        letter = 'A'
    elif percent >= 80:
        letter = 'B'
    elif percent >= 70:
        letter = 'C'
    elif percent >= 60:
        letter = 'D'
    else:
        return 'F'
    if suffix:
        if letter == 'A' and percent > 99:
            letter += '+'
        elif letter != 'F':
            if percent % 10 >= 7:
                letter += '+'
            elif percent % 10 < 3:
                letter += '-'
    return letter

def round_half_up(number):
    """Round number up if ends in .5 or above and down otherwise."""
    if number % 1 >= 0.5:
        return ceil(number)
    else:
        return floor(number)
