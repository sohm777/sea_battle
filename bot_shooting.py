'''алгоритм выстрелов компьютреа по кораблям игрока'''

import random

prev_shot = []

def botShot(ship_plr, ship_plr_shot, fleet_plr):
    '''print('заходит в >>>>>>>>>> bot_shot')
    for i in fleet_plr:
        print(i)
    print('<'*30)'''
    global prev_shot
    shooted = 0
    dead = 0
    while True:
        # флаг конца игры и победы компьютера
        end = False
        if prev_shot:
            print('предыдущие выстрелы =>', prev_shot)
            # точный выстрел, если в предыдущем попал
            x, y = aptShot(prev_shot, fleet_plr)
            shot = [x, y]
        else:
            # первый случайный выстрел
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            shot = [x, y]
            print('случайный выстрел =>', shot)
        # если попал
        if fleet_plr[x][y] == 3:
            fleet_plr[x][y] = 2
            shooted += 1
            print('-'*30)
            print('БОТ попал выстрелом =>', shot)
            print('флот игрока до выстрела')
            for i in ship_plr:
                print(i)
            for ship in ship_plr:
                if shot in ship:
                    print('БОТ попал в корабль =>',ship,
                          '\nиндекс =>',ship_plr.index(ship))
                    index_ship = ship_plr.index(ship)
                    ship.remove([x, y])
                    # значение для след.выстрела
                    prev_shot.append(shot)
                    # проверить корабль на затопление
                    if len(ship) == 0:
                        dead += 1
                        #index_ship = ship_plr.index(ship) ???
                        ship_shot = ship_plr_shot[index_ship]
                        print('БОТ ПОТОПИЛ =>', ship_shot,
                              'выстрелом', shot,
                              '\nиндекс потопленного =>',index_ship)
                        # очерчивание потопленного корабля игрока
                        drowned(ship_shot, fleet_plr)
                        # очистка предыдущего выстрела
                        prev_shot = []
                        # проверка на победу компьютера и конец игры
                        end = True
                        for k in ship_plr:
                            if k:
                                end = False
                        print('end ==>', end)
                        if end:
                            return (x, y, ship_plr, ship_plr_shot,
                                    fleet_plr, shooted, dead, end)

            print('флот игрока после выстрела')
            for i in ship_plr:
                print(i)
            print('<'*30)
            
        # промазал
        elif fleet_plr[x][y] == 5:
            fleet_plr[x][y] = 1
            print('БОТ промазал =>', shot)
            print('<'*30)
            return (x, y, ship_plr, ship_plr_shot,
                    fleet_plr, shooted, dead, end)

# очерчивание потопленного корабля игрока
def drowned(ship_shot, fleet_plr):
    for deck in ship_shot:
        x, y = deck[0], deck[1]
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if 9>=i>=0 and 9>=j>=0:
                    if fleet_plr[i][j]==5 or fleet_plr[i][j]==6:
                        fleet_plr[i][j]=1
    print('очерчен корабль', ship_shot)
    return fleet_plr

# точный выстрел
def aptShot(prev_shot, fleet_plr):
    # было попадание только в одну палубу
    if len(prev_shot) == 1:
        x, y = prev_shot[0][0], prev_shot[0][1]
        possible = [[x-1,y], [x,y+1], [x+1,y], [x,y-1]]    
    # корабль по х
    elif prev_shot[0][0] == prev_shot[1][0]:
        rand_deck = random.choice(prev_shot)
        x, y = rand_deck[0], rand_deck[1]
        possible = [[x,y+1], [x,y-1]]
    # корабль по y
    elif prev_shot[0][1] == prev_shot[1][1]:
        rand_deck = random.choice(prev_shot)
        x, y = rand_deck[0], rand_deck[1]
        possible = [[x-1,y], [x+1,y]]
    # проверка на невыход за поле
    for i in possible:
        for j in i:
            if j < 0 or j > 9:
                possible.remove(i)
    rand_shot = random.choice(possible)
    print('точный выстрел =>', [rand_shot[0], rand_shot[1]])
    return rand_shot[0], rand_shot[1]
