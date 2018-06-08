
from enemy import enemy
import random
#Monster 4 CLASS
class dragon(enemy):
    def __init__(self):
        super().__init__(50,"dragon",20)
    #decides a random super or regular attack
    def attack(self,opponent):
        attack_number = random.randint(0,2)
        if attack_number == 1:
            self.regularattack(opponent)
        else:
            self.superattack(opponent)
    def regularattack(self,opponent):
        self.setAttack(20)
        opponent.damaged(self)
        print("THE DRAGON SHOOTS WHITE HOT EMBERS AT YOU")
    def superattack(self,opponent):
        self.setAttack(40)
        opponent.damaged(self)
        print("THE DRAGON LAUNCHES AN INFERNO OF 10 SUNS AT YOU")
    def damaged(self,damage):
        self.setHealth(self.getHealth()-damage)