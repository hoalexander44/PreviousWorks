#This is a rpg battle program where the player and the enemy can switch between attacking
import random
from hero import hero
from dragon import dragon
from ogre import ogre
from goblin import goblin
from slime import slime
random.seed(0)
#Function that creates the battle
def battle(hero,opponent):
    stopper = 0
    print(opponent)
    while stopper == 0:
        if opponent.getHealth()<=0:
            print("You win!")
            return (True)
            stopper = 1
        elif hero.getHealth()<=0:
            print("You LOSE")
            return (False)
            stopper = 1
        else:
            hero.attack(opponent)
            print(opponent)
            if opponent.getHealth() > 0:
                opponent.attack(hero)
            
if __name__ == "__main__":
    e = hero(100,"cloud",10,10,6)
#initial start up stuff
    print ("Welcome to Adventure Battle!")
    hero_name = input("What is the name of your hero?")
    e.setName(hero_name)
    monster_amount = int(input("How many monsters will your hero battle?\n"))
    stopper = 0
#loops battle until player loses or player wins
    for i in range(0,monster_amount):
        stopper = 0
        while stopper == 0:
            monster_number = random.randint(0,3)
            if monster_number == 0:
                f = slime()
            elif monster_number ==1:
                f = goblin()
            elif monster_number ==2:
                f = dragon()
            elif monster_number ==3:
                f = ogre()
            result = battle(e,f)
            if result == False:
               stopper = 1
            else:
                stopper = 1
                pass
    
    

    
