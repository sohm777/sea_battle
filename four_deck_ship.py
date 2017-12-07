'''установка четырёхпалубного корабля'''

import random
from decks import secondDeck, thirdDeck, fourthDeck, inactiveArea

def four(fleet):
    # определение всех переменных координат
    '''выбор первой палубы'''
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
    fleet[x1][y1] = 2
    '''выбор второй палубы'''
    fleet, x2, y2 = secondDeck(fleet, x1, y1)
    '''выбор третей палубы'''
    fleet, x3, y3 = thirdDeck(fleet, x1, y1, x2, y2)
    '''выбор четвёртой палубы'''
    fleet, x4, y4 = fourthDeck(fleet, x1, y1, x2, y2, x3, y3, 4)
    '''очерчевание корабля неактивной областью'''
    inactiveArea(fleet, x1, y1, x2, y2, x3, y3, x4, y4)
    ship = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
    ship.sort()
    return ship, fleet

if __name__ == '__main__':
    fleet = [ [0 for j in range(10)] for i in range(10)]
    four(fleet)
