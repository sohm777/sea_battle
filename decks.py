'''постоение отдельных палуб'''

import random

def rand(x, y, fleet, prev_x=None, prev_y=None, deckship=None):
    while True:
        # определяется номер палубы, которая строится
        # если пред. х и у нет - строится вторая палуба, есть - третья
        if (prev_x is None) and (prev_y is None):
            next_x = random.randint(x-1, x+1)
            next_y = random.randint(y-1, y+1)
        elif prev_x == x and deckship is None:
            next_x = x
            next_y = random.randint(y-2, y+2)
        elif prev_y == y and deckship is None:
            next_x = random.randint(x-2, x+2)
            next_y = y
        # если строится четвёртая палуба
        elif prev_x == x and deckship == 4:
            next_x = x
            next_y = random.randint(y-3, y+3)
        elif prev_y == y and deckship == 4:
            next_x = random.randint(x-3, x+3)
            next_y = y
        # проверка на пустую клетку
        if 9>=next_x>=0 and 9>=next_y>=0:
            if fleet[next_x][next_y] == 0:
                # проверка на неразрывность
                # проверка, если корабль на линии х
                if next_x == x:
                    if prev_x is None:
                        # строится ВТОРАЯ X ячейка
                        # проверка на пустую третью ячейку для 3-х палубного
                        # при выбранной второй
                        if deckship is None:
                            if 9>=y-2>=0 and (fleet[x][y-2] == 0):
                                return next_x, next_y
                            elif 9>=y+2>=0 and (fleet[x][y+2] == 0):
                                return next_x, next_y
                        # проверка на пустую или неактивную клетку
                        # для ВТОРОЙ палубы 2-х палубного
                        if deckship == 2:
                            if 9>=y-1>=0 and (fleet[x][y-1] == 0 or
                                              fleet[x][y-1] == 1):
                                return next_x, next_y
                            elif 9>=y+1>=0 and (fleet[x][y+1] == 0 or
                                                fleet[x][y+1] == 1):
                                return next_x, next_y
                    # если строится ТРЕТЬЯ или ЧЕТВЁРТАЯ палуба
                    elif y > prev_y:
                        # для ТРЕТЬЕЙ палубы 3-палубного
                        if deckship is None:
                            y_min = y-2
                            y_max = y+1
                        # для ЧЕТВЁРТОЙ палубы
                        elif deckship == 4:
                            y_min = y-3
                            y_max = y+2
                        # проверка на невыход за поле
                        if y_min>=0 or y_max<=9:
                            if (y_min)<=next_y<=(y_max):
                                return next_x, next_y
                    elif y < prev_y:
                        # для ВТОРОЙ палубы 3-палубного
                        if deckship is None:
                            y_min = y-1
                            y_max = y+2
                        # для ЧЕТВЁРТОЙ палубы
                        elif deckship == 4:
                            y_min = y-2
                            y_max = y+3
                        # проверка на невыход за поле
                        if (y_min>=0) or (y_max<=9):
                            if (y_min)<=next_y<=(y_max):
                                return next_x, next_y
                # проверка, если корабль на линии y
                elif next_y == y:
                    if prev_y is None:
                        # строится ВТОРАЯ Y ячейка 3-х палубного
                        # проверка на пустую третью ячейку для 3-х палубного
                        # при выбранной второй
                        if deckship is None:
                            if 9>=x-2>=0 and (fleet[x-2][y] == 0):
                                return next_x, next_y
                            elif 9>=x+2>=0 and (fleet[x+2][y] == 0):
                                return next_x, next_y
                        if deckship == 2:
                            if 9>=x-1>=0 and (fleet[x-1][y] == 0):
                                return next_x, next_y
                            elif 9>=x+1>=0 and (fleet[x+1][y] == 0):
                                return next_x, next_y
                    # если строится ТРЕТЬЯ палуба
                    # в зависимости от расположения предыдущей палубы
                    elif x > prev_x:
                        # для ТРЕТЬЕЙ палубы 3-палубного
                        if deckship is None:
                            x_min = x-2
                            x_max = x+1
                        # для ЧЕТВЁРТОЙ палубы
                        elif deckship == 4:
                            x_min = x-3
                            x_max = x+2
                        # проверка на невыход за поле
                        if x_min>=0 or x_max<=9:
                            if x_min<=next_x<=x_max:
                                return next_x, next_y
                    elif x < prev_x:
                        # для ВТОРОЙ палубы 3-палубного
                        if deckship is None:
                            x_min = x-1
                            x_max = x+2
                        # для ЧЕТВЁРТОЙ палубы
                        elif deckship == 4:
                            x_min = x-2
                            x_max = x+3
                        # проверка на невыход за поле
                        if x_min>=0 or x_max<=9:
                            if x_min<=next_x<=x_max:
                                return next_x, next_y

def mx(*args):
    # +1 - потому что проверяется предполагаемая ячейка у3=max+1
    return max(args)+1

def mn(*args):
    # -1 - потому что проверяется предполагаемая ячейка у3=min-1
    return min(args)-1
        
'''выбор второй палубы'''
def secondDeck(fleet, x1, y1, deckship=None):
    x2, y2 = rand(x1, y1, fleet, None, None, deckship)
    fleet[x2][y2] = 2
    return fleet, x2, y2

'''выбор третей палубы'''
def thirdDeck(fleet, x1, y1, x2, y2):
    x3, y3 = rand(x2, y2, fleet, x1, y1)
    fleet[x3][y3] = 2
    return fleet, x3, y3

'''выбор четвёртой палубы'''
def fourthDeck(fleet, x1, y1, x2, y2, x3, y3, deckship):
    # проверка на неразрыв 4 корпуса
    while True:
        x4, y4 = rand(x3, y3, fleet, x2, y2, deckship)
        if (x4 == mn(x1,x2,x3) or x4 == mx(x1,x2,x3) or
            y4 == mn(y1,y2,y3) or y4 == mx(y1,y2,y3)):
            fleet[x4][y4] = 2
            return fleet, x4, y4

'''очерчевание корабля неактивной областью'''
def inactiveArea(fleet, x1, y1, x2=None, y2=None,
                  x3=None, y3=None, x4=None, y4=None):
    ship = ((x1,y1),(x2,y2),(x3,y3),(x4,y4))
    for k in ship:
        x, y = k[0], k[1]
        if (x is not None) and (y is not None):
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if 9>=i>=0 and 9>=j>=0:
                        if fleet[i][j]==0:
                            fleet[i][j]=1
    return fleet
