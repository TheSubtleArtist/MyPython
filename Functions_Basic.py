'''
Create a program that will track what Agent S likes in their hot drink from the cafe. Try and split apart your program into smaller functions.
Regular coffee, decaf coffee, lattes, and flat whites always get 2 sugars.
Regular coffee and decaf coffee get milk.
Earl Grey tea gets lemon and 1 sugar
Other types of black tea get milk and 1 sugar
Green tea doesn't get anything
Espresso doesn't get anything

'''
Agent = 'S'
drinks={

    'coffee':['2 sugars', 'milk', 'muffin'],
    'decaf coffee':['2 sugars', 'milk', 'muffin'],
    'latte':['2 sugars'],
    'flat white':['2 sugars'],
    'earl grey':['lemon', '1 sugar'],
    'black tea':['milk', '1 sugar', 'scone'],
    'green tea':['scone' ],
    'espresso':['plain']
}



def greetAgent(agent):
    print(f"Hellow Agent {agent}, your drinks are:")
  
def agentDrinks():
    for key, value in drinks.items():
        print(key.title() + ' with:')
        [print('  ',each.title()) for each in value]    


if __name__ == '__main__':
    greetAgent(Agent)
    print(agentDrinks())