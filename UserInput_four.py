'''
Give this example code a few tries in the code editor below with different inputs to see if you can trip it up. 
One way it is still flawed is that you can't give it an answer like 2.5 and have it understand that user input as a float: 
it will see that answer as a string and give you an error, even though 2.5 can be compared to 2 using the > operator. 
How would you fix this?

Currently, if this program can't understand your answer because it's a string, it gives you an error message and you have to re-run it to try again. 
How would you incorporate a loop into this code so that the program will ask again if it doesn't understand your answer? 
Hint: this is a great use case for a while loop and a flag!

If the program asks you if you want to get coffee, have it get user input where if you reply with "yes" it responds with "Ok, let's go!", 
and if you respond with "no" it responds "Ok, see you later." 
And if don't respond with either "yes" or "no", it should ask you again since it didn't understand the answer you gave it.
'''

# Checks if the user's answer can be used by the determineReply() 
# function, and if it cannot provides an error.
def get_reply(user_input):
    flag = False
    while flag == False:
        if user_input.isdigit():
            user_input_int = int(user_input)
            Flag = True
            return determine_reply(user_input_int)
        else:
            user_input = input('Sorry, I don\'t understand your answer. I was looking for a number, not a string. Try Again')

# Determines the correct reply
def determine_reply(user_input_int):
    if user_input_int > 2:
        return 'Wow, that\'s a lot of coffee!'
    elif user_input_int == 0:        
        aFlag = False
        while aFlag == False:
            asked = input('Should we go grab a coffee? I could use one too. Yes (Y) or No (N)')
            asked = asked.upper() 
            if asked == 'Y':
                aFlag = True
                return "Great, Let's Go"
            elif asked == 'N':
                aFlag == True
                return 'Okay, see you later'
            else:
                print('I didn\'t understand your input. Please try again')
    else:
        return 'Sounds like the right amount of coffee to start the day.'



if __name__ == '__main__':
    mainFlag = True
    while mainFlag == True:
        # Ask for user input
        user_coffee_input = input('How many cups of coffee have you had today? ')
        # Process the answer to get the right reply, and print that reply
        reply = get_reply(user_coffee_input)
        print(reply)
        repeat = input('Try again? Press \'Y\' for yes, any other character to quit.')
        repeat = repeat.upper()
        if repeat != 'Y':
            mainFlag = False
            print("Goodbye")
