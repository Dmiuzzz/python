import time
from itertools import cycle


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        d = int(input("Введите количество итераций "))
        c = 0
        if self.__color == 'красный':
            dict = {'красный': 7, 'желтый': 2, 'зеленый': 5}
        elif self.__color == 'желтый':
            dict = {'желтый': 2, 'зеленый': 5, 'красный': 7}
        elif self.__color == 'зеленый':
            dict = {'зеленый': 5, 'красный': 7, 'желтый': 2}
        for el in cycle(dict):
            print(el)
            time.sleep(dict.get(el))
            if d <= c:
                break
            else:
                d -= 1

traff_l = TrafficLight('красный')
traff_l.running()