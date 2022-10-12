from random import choice, random
from abc import ABC, abstractmethod

# 1 varför inga getters and setters - 
#   det blir mer på ChristmasPresent

# Access modifiers
#               __ 
# 1.5 public vs private vs protected

# 2 abstract

class GameObject(ABC):
    def __init__(self, name:str):
        self._name = name  
        self._level = 0
    @abstractmethod
    def Act(self):
        pass

class Fly (GameObject):
    def __init__(self, name:str, color:str ):
        super().__init__(name)
        self.__color = color

    def Act(self):
        actions = ["surrar", "landar i maten", "flyger"]
        action = choice(actions)
        print(f"{self._name} {action}")


class Person(GameObject):
    def __init__(self, name:str ):
        super().__init__(name)
        self.__lastAction = ""

    def Act(self):
        actions = ["äter", "rapar", "funderar", "dricker"]
        action = choice(actions)
        self.MightLevelUp(action)
        print(f"{self._name} {action}")
        self.__lastAction = action

    def MightLevelUp(self,action:str):
        if action  == "rapar" and self.__lastAction == "rapar":
            self._level = self._level + 1
            print(f"!!!LEVEL UP!!! {self._level}")



stefan = Person("Stefan")
kerstin = Person("Kerstin")
oliver = Person("Oliver")
fly = Fly("Fula flugan", "blå")


deltagare = [stefan,kerstin,oliver,fly]

while True:
    for person in deltagare:
        person.Act()
        
