# Create a game that uses 2 classes: Hero() and Monster().
# damage strength and starting health points that you choose.




class hero():

    '''
    The hero:
    Has a weapon that does an amount of damage
    Has an amount of health
    Can attack with their weapon and cause damage
    Can lose health if attacked
    Will die if they have 0 health
    Has 1 healing potion that they can drink to get back 5 health, but the potion can only be used once.
    '''

    def __init__(self, weapon, heroHealth, potion):
        self.weapon = weapon
        self.heroHealth = heroHealth
        self.potion = potion

    def drinkPotion(self):
        self.heroHealth +=5
        self.potion -= 1

    def receiveAttack(self):
        self.heroHeatlh -= 3
        if self.heroHealth <= 0:
            self.dieHero(self)

    def dieHero(self):
        print("Hero has died.")
    
    def attackEnemy(self):
        print('Hero Attacks')



class monster():

    '''
    The monster:
    Has an attack strength and can do an amount of damage
    Has an amount of health
    Can roar
    Can attack and cause damage
    Can lose health if attacked
    Will automatically run away if it gets down to 1 health remaining
    '''

    def __init__(self, attackValue, monsterHealth):
        self.attackValue = attackValue
        self.monsterHealth = monsterHealth

    def monsterRoar(self):
        print('MONSTER ROAR')

    def attackEnemy(self):
        print('Monster Attacks')


    def receiveAttack(self):
        self.monsterHealth -= 3
        if self.monsterHealth <= 1:
            self.monsterRun()    
    
    def monsterRun(self):
        print('Monster has run away')

if __name__ == "__main__":

    gdzla = hero(weapon = 3, heroHealth = 20, potion = 1)
    mthra = monster(attackValue = 3, monsterHealth = 25)

