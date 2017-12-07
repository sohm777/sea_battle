'''постройка 2-палубного корабля'''

import random
from decks import secondDeck, inactiveArea

def two(fleet):
    '''выбор первой палубы'''
    while True:
        x1 = random.randint(0, 9)
        y1 = random.randint(0, 9)
        # проверка на пустую ячейку
        if fleet[x1][y1] == 0:
            # возможности размещения корабля
            v_sh_1 = []
            v_sh_2 = []
            v_sh_3 = []
            v_sh_4 = []
            for i in range(x1-1,x1):
                if 9>=i>=0:
                    if fleet[i][y1] == 0:
                        v_sh_1.append((i,y1))
            for i in range(x1+1,x1+2):
                if 9>=i>=0:
                    if fleet[i][y1] == 0:
                        v_sh_2.append((i,y1))
            for i in range(y1-1,y1):
                if 9>=i>=0:
                    if fleet[x1][i] == 0:
                        v_sh_3.append((x1,i))
            for i in range(y1+1,y1+2):
                if 9>=i>=0:
                    if fleet[x1][i] == 0:
                        v_sh_4.append((x1,i))
            if len(v_sh_1) == 1:
                break
            if len(v_sh_2) == 1:
                break
            if len(v_sh_3) == 1:
                break
            if len(v_sh_4) == 1:
                break
    fleet[x1][y1] = 2
    '''выбор второй палубы'''
    fleet, x2, y2 = secondDeck(fleet, x1, y1, 2)
    ship = [[x1, y1], [x2, y2]]
    ship.sort()
    '''очерчевание корабля неактивной областью'''
    inactiveArea(fleet, x1, y1, x2, y2)
    return ship, fleet
