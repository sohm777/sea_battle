'''строится 3-палубный корабль'''

import random
from decks import secondDeck, thirdDeck, inactiveArea

def virtShip(x, y, fleet):
    virt = []
    for i in range(x-2,x+1):
        virt.append((i,y))
    return virt

def three(fleet):
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
            for i in range(x1-2,x1):
                if 9>=i>=0:
                    if fleet[i][y1] == 0:
                        v_sh_1.append((i,y1))
            if len(v_sh_1) == 2:
                break
            
            for i in range(x1+1,x1+3):
                if 9>=i>=0:
                    if fleet[i][y1] == 0:
                        v_sh_2.append((i,y1))
            if len(v_sh_2) == 2:
                break
            
            for i in range(y1-2,y1):
                if 9>=i>=0:
                    if fleet[x1][i] == 0:
                        v_sh_3.append((x1,i))
            if len(v_sh_3) == 2:
                break
            
            for i in range(y1+1,y1+3):
                if 9>=i>=0:
                    if fleet[x1][i] == 0:
                        v_sh_4.append((x1,i))
            if len(v_sh_4) == 2:
                break
    fleet[x1][y1] = 2
    '''выбор второй палубы'''
    fleet, x2, y2 = secondDeck(fleet, x1, y1)
    '''выбор третей палубы'''
    fleet, x3, y3 = thirdDeck(fleet, x1, y1, x2, y2)
    '''очерчевание корабля неактивной областью'''
    ship = [[x1, y1], [x2, y2], [x3, y3]]
    ship.sort()
    inactiveArea(fleet, x1, y1, x2, y2, x3, y3)
    return ship, fleet

if __name__ == '__main__':
    fleet = [ [0 for j in range(10)] for i in range(10)]
    three(fleet)
