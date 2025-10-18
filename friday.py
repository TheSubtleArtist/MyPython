from datetime import date

# 0 means Monday, 1 means Tuesday, etc.
if date.today().weekday() == 4:
    print("FRIDAY")