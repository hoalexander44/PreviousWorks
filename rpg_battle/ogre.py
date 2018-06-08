
from enemy import enemy
#Monster 3 CLASS
#ogre monster distinct attribute values , can attack and do damage
class ogre(enemy):
    def __init__(self):
        super().__init__(30,"ogre",15)
    def attack(self,opponent):
        opponent.damaged(self)
        print("The ogre smashes you!")
    def damaged(self,damage):
        self.setHealth(self.getHealth()-damage)