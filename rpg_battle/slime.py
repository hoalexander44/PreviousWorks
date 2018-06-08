
from enemy import enemy
import random
#Monster 1 CLASS
class slime(enemy):
    def __init__(self):
        super().__init__(5,"slime",2)
    #decides a random super or regular attack
    def attack(self,opponent):
        attack_number = random.randint(0,2)
        if attack_number == 1:
            self.regularattack(opponent)
        else:
            self.superattack(opponent)
    def regularattack(self,opponent):
        self.setAttack(2)
        opponent.damaged(self)
        print("THE SLIME SLAMS ON YOU BOI")
    def superattack(self,opponent):
        self.setAttack(10)
        opponent.damaged(self)
        print("THE SLIME MEGA MEGA MEGA MEGA SLAMS  ON YOU")
    def damaged(self,damage):
        self.setHealth(self.getHealth()-damage)