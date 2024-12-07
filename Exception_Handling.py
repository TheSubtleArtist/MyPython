"""
There is at least one more exception that can easily happen in the provided code on this page. 
What happens if, instead of a number, we type a letter or a word, like "five" or "apple"? 
Revise the code to handle this user error as well so the program doesn't crash.


"""
from pickle import TRUE


def validateInput(userInput):
    flag = False
    while flag == False:
        try:
            userInput = int(userInput)
            flag = True
        except:
            userInput=input("Not an integer, please enter another value")
    return userInput




print('Please give me 2 numbers and I will divide them.')
print('Enter "q" to quit.\n')

while True:
    first_number = input('First Number: ')
    if first_number == 'q':
        break
    else:
        first_number = validateInput(first_number)

    second_number = input('Second Number: ')
    if second_number == 'q':
        break
    else:
        second_number = validateInput(second_number)

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can\'t divide by zero! Let\'s start again.')
    else:
        print('Your answer is: ' + str(answer))
        print('Give me another!\n')

print('Ok, bye!')
