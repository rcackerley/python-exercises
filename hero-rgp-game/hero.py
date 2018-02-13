from random import *

class Character(object):
    def __init__(self, health, power, coins, armor):
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = armor
    def alive(self):
        if self.health > 0:
            return True
    def attack(self, character):
        character.health -= self.power
        print "%d damage done." % self.power
    def print_status(self):
        return  "%d health and %d power." % (self.health, self.power)

class Hero(Character):
    def __init__(self, health, power, coins, armor, evade):
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = armor
        self.evade = evade
    def attack(self, character):
        roll = randint(1, 5)
        if roll == 1:
            character.health -= (self.power * 2)
            print "%d damage done Doubled!." % (self.power * 2)
        else:
            super(Hero, self).attack(character)
    def print_status(self):
        print "You have " + super(Hero, self).print_status()
    
    

class Goblin(Character):
    def print_status(self):
        print "The goblin has " + super(Goblin, self).print_status()

class Zombie(Character):
    def alive(self):
        if self.health > 0 or self.health < 0:
            return True
    def print_status(self):
        print "The zombie has" + super(Zombie, self).print_status()

class Medic(Character):
    def heal(self):
        roll = randint(1, 5)
        if roll == 1:
            self.health += 2
            print 'The Medic has healed itself 2 Health!'
    def print_status(self):
        print "The medic has " + super(Medic, self).print_status()

class Shadow(Character):
    def dodge(self):
        roll = randint(1,10)
        if roll < 10:
            return True
    def print_status(self):
        print "The shadow has " + super(Shadow, self).print_status()
    
class Alchemist(Character):
    def brew(self):
        roll = randint(1,4)
        if roll == 1:
            self.health += 3
            self.power += 2
            print 'The Alchemist has brewed a potion enhancing his power and restoring some health!'
    def print_status(self):
        print "The alchemist has " + super(Alchemist, self).print_status()

class God(Character):
    def infinite(self, character):
        roll = randint(1,10)
        if roll == 1:
            character.health -= 1000
            print 'The god has grown tired of toiling with you. 1000 damage done. Goodbye'
    def print_status(self):
        print "The god has " + super(God, self).print_status()

class item():
    def __init__(self, name):
        self.name = name

class Potion(item):
    def drink(self):
        self.health += 10

class Armor(item):
    def purchaseArmor(self):
        self.armor += 2

class Evasion(item):
    def evade(self):
        self.evade += 2


hero = Hero(10, 3, 0, 0, 0)
goblin = Goblin(20, 2, 1, 0)
zombie = Zombie(100,1, 2, 0)
medic = Medic(14, 2, 3, 0)
shadow = Shadow(1, 6, 9, 0)
alchemist = Alchemist(12, 2, 12, 0)
god = God(400, 0, 1000000000, 0)
            
"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
#Main Menus
def menu():
    print '''
    Main Menu
    ==========
    1. Go to Store
    2 Start Battle
    '''
    choice = raw_input('How would you like to proceed?').lower()
    if choice == '1' or choice == 'store' or choice == 'go to store':
        print ''''
    What would you like to purchase?
    1. Potion - Cost 2 Coins
    2. Armor - Cost 2 Coins
    3. Evasion - Cost 2 Coins
    
    You have %d coins''' % hero.coins
        choice = raw_input()
        if choice == '1':
            if hero.coins >= 2:
                hero.potion += 10
                print 'You have purchased a potion.' 
            elif hero.coins < 2:
                print 'You do not have enough coins to purchase'
                menu()
        elif choice == '2':
            if hero.coins >= 2:
                hero.armor += 2
                print 'You now have %d armor.' % hero.armor
            elif hero.coins < 2:
                print 'You do not have enough coins to purchase'
                menu()
        elif choice == '3':
            if hero.coins >= 2:
                hero.Evasion += 2
                print 'You now have %d evasion points' % hero.evade
            elif hero.coins < 2:
                print 'You do not have enough coins to purchase'
                menu()
        else:
            'That is not a valid choice. Please input a valid number.'
            menu()
    elif choice == '2' or choice == 'battle' or choice == 'start battle':
        main()

#Battle
def main():
    while alchemist.alive() and hero.alive():
        hero.print_status()
        alchemist.print_status()
        print "What do you want to do?"
        print "1. fight the alchemist"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            # Hero attacks shadow
            hero.attack(alchemist)
            if alchemist.alive() is not True:
                print "The alchemist is dead."
                hero.coins += alchemist.coins
                print 'You have %s coins' % hero.coins
            else: 
                alchemist.brew()
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if alchemist.alive():
            # Medic attacks hero
            alchemist.attack(hero)
            if hero.alive() is not True:
                print "You are dead."


menu()

