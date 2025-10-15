import sys

def altprint(text):
    """Print text in aLtErNaTiNg CaPiTaLiZaTiOn."""
    result = ""
    capitalize_next = False
    for char in text:
        if char.isalpha():
            if capitalize_next:
                result += char.upper()
            else:
                result += char.lower()
            capitalize_next = not capitalize_next
        else:
            result += char
    sys.stdout.write(result + "\n")