'''постройка однопалубного корабля'''

import random
from decks import inactiveArea

def one(fleet):
    while True:
        x1 = random.randint(0, 9)
        y1 = random.randint(0, 9)
        # проверка на пустую ячейку
        if fleet[x1][y1] == 0:
            break
    fleet[x1][y1] = 2
    ship = [[x1, y1]]
    inactiveArea(fleet, x1, y1)
    return ship, fleet
