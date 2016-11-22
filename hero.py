# coding: utf-8
# license: GPLv3
from gameunit import *

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
class Attacker:
    _health = None
    _attack = None



class Hero(Attacker):
    def __init__(self,name):
        self._health=100
        self._attack=50
        self._experience=0
        self._name= name

    def attack(self, target):
        target._health -= self._attack
        target._experience += self._attack

    def is_alive(self):
        return self._health > 0