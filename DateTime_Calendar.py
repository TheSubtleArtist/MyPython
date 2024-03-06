"""
The calendar module allows you to output calendars and provides additional useful functions for them.
class calendar.TextCalendar([firstweekday])
This class can be used to generate plain text calendars.

Task
You are given a date(in MM DD YYYY format). Your task is to find what the day is on that date.
"""
import calendar

# Take the input values
m, d, y = map(int, input().split())


# use calendar.weekday() to determine the day of the week represented by the inputs. Outputs as an integeger
#feed the integer to calendar.day_name to change the integer into the name of the day of the week
print((calendar.day_name[calendar.weekday(y,m,d)]).upper())