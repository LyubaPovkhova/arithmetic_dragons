# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 20
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 20
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 20
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest





class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class BlueTroll(Troll):
    def __init__(self):
        self._health = 20
        self._attack = 10
        self._color = 'синий'

    def question(self):
        x = randint(1,5)
        self.__quest = "Угадай число от 1 до 5"
        self.set_answer(x)
        return self.__quest
class WhiteTroll(Troll):
    def __init__(self):
        self._health = 20
        self._attack = 10
        self._color = 'белый'

    def question(self):
        x = randint(1,100)
        self.__quest = 'Является ли число' + str(x) + 'простым?'
        for i in range (1,x-1):
            if x%i = 0:
                self.set_answer(False)
            else:
                self.set_answer(True)
        return self.__quest





enemy_types=[BlueTroll, WhiteTroll, GreenDragon, RedDragon, BlackDragon]


