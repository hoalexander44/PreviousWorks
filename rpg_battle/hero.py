
from enemy import enemy
#HERO CLASS
class hero(enemy):
    def __init__(self,health,name,attack,ammo,potions):
        super().__init__(health,name,attack)
        self.__maxhealth = health
        self.__ammo = ammo
        self.__potions = potions
        self.__firedamage = 100
        #decides how much damage player takes, if it is on player takes half amount of damage
        self.__shielding = False
    #attack method allows the player to decide between using a sword, fireball, potion, shield, or exiting
    def attack(self,opponent):
        print(self.getName(),":", self.getHealth(),"/",self.__maxhealth,"health")
        print("Remaining:",self.__ammo," Fireballs,",self.__potions,"Potions")
        stopper = 0
        while stopper ==0:
            self.__shielding = False
            attack_type = input("Enter Command: sword shield fireball potion exit \n")
            if attack_type.lower() == "sword":
                self.sword(self.getAttack(),opponent)
                print("You attacked with your sword!")
                stopper = 1
            elif attack_type.lower() == "fireball":
                if self.__ammo >= 1:
                    self.fireball(self.__firedamage,opponent,self.__ammo)
                    print("You shot a fireball!")
                    stopper = 1
                else:
                    print("Not enough fireballs!")
            elif attack_type.lower() == "shield":
                self.__shielding = True
                print("You put up your shield!")
                stopper = 1
            elif attack_type.lower() == "exit":
                print("Thanks for Playing")
                exit()
                stopper = 1
            elif attack_type.lower() == "potion":
                if self.__potions >=1 and self.getHealth()<self.__maxhealth:
                    self.potion()
                    print("You used a potion!")
                    stopper = 1
                else:
                    print("You are either at max health or you do not have enough potions")
    #the actual methods of sword, fireball, shield, potion, and exit
    def sword(self,attack,opponent):
        opponent.damaged(attack)
    def fireball(self,attack,opponent,ammo):
        opponent.damaged(attack)
        self.__ammo = self.__ammo - 1
    def shield(self,opponent):
        self.setHealth(self.getHealth() - opponent.getAttack()/2)
    def potion(self):
        self.setHealth(self.getHealth()+10)
        if self.getHealth() > self.__maxhealth:
            self.setHealth(100)
        self.__potions -=1
    def damaged(self,opponent):
        if self.__shielding == False:
            self.setHealth(self.getHealth()-opponent.getAttack())
        else:
            self.shield(opponent)
    #mainly for debugging purposes, sees if player is shielding and sees if it is turned off the next turn
    def getShielding(self):
        return(self.__shielding)