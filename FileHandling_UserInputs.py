'''
Create a program that accepts user input and allows you to add places to a text file that you'd like to travel to. The program should:

Create the file and call it travel-bucket-list.txt if it doesn't already exist.
Ask you Where would you like to travel? as a user prompt.
Add the answer you give it to the list you've saved in your text file.
Say Great, I've added to your list! Anywhere else? and offer you an input to add more.
Allow you to quit the program if you type the word quit and say Ok, goodbye! when it quits.



'''
with open('travel-bucket-list.txt', 'a') as file:
    flag = True
    location = input('To where would you like to travel?')
    while flag:
        file.write(location.title())
        print(f'{location.strip().title()} added to the list.')
        location = input("Enter another location, or  'quit' to end.")
        location = location.title()
        if location == 'Quit':
            flag = False
    print("Ok, goodbye!")

