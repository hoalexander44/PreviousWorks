
from enemy import enemy
#Monster 2 CLASS
#goblin monster distinct attribute values , can attack and do damage
class goblin(enemy):
    def __init__(self):
        super().__init__(15,"goblin",5)
    def attack(self,opponent):
        opponent.damaged(self)
        print("The goblin insults you!")
    def damaged(self,damage):
        self.setHealth(self.getHealth()-damage)