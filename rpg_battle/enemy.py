
import abc
import random
#Base Class
class enemy(metaclass = abc.ABCMeta):
    #abstract methods
    @abc.abstractmethod
    def damaged(self):
        pass
    @abc.abstractmethod
    def attack(self):
        pass
    #the main attributes and methods
    def __init__(self, health, name, attack):
        self.__health = health
        self.__name = name
        self.__attack = attack
    def setName(self, name):
        self.__name = name
    def setHealth(self, health):
        self.__health = health
    def getName(self):
        return(self.__name)
    def getHealth(self):
        return(self.__health)
    def getAttack(self):
        return(self.__attack)
    def setAttack(self,attack):
        self.__attack = attack
    def __str__(self):
        a = "Monster: "
        b = "Health: "
        c = str(self.getHealth())
        d = str(self.getName())
        return (str(a+d+" "+b+" "+c))