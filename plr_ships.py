'''проверка правильности расстановки флота игроком'''

# соответствие индекса корабля к кол-ву его палуб
ind = {0:4, 1:3, 2:3, 3:2, 4:2, 5:2, 6:1, 7:1, 8:1, 9:1, 10:5}

# проверка на мёртвую зону
def checkDeadZone(x, y, ship_plr, fleet_plr):
    # очистка от неактивных ячеек - все ячейки 0
    for i in range(10):
        for j in range(10):
            if fleet_plr[i][j] == 5:
                fleet_plr[i][j] = 0
    for ship in ship_plr:
        sum_deck = ind[ship_plr.index(ship)]
        # определение строящегося корабля
        if len(ship) < sum_deck:
            print('ship =>', ship)
            # если строится 3-х или 2-х палубный
            if 0 < ship_plr.index(ship) < 6:
                # проверка, влезет ли корабль в выбранное место
                if deadZone(x, y, ship, ship_plr,
                             fleet_plr, sum_deck):
                    print('РАЗРЕШЕНО')
                    return plrCheck(x, y, ship, ship_plr, fleet_plr)
                else:
                    print('ЗАПРЕЩЕНО')
                    return ship_plr, str(sum_deck), False
            else:
                return plrCheck(x, y, ship, ship_plr, fleet_plr)

# построение плубы и очерчивание целого корабля
def plrCheck(x, y, ship, ship_plr, fleet_plr):
    sum_deck = ind[ship_plr.index(ship)]
    ship.append([x, y])
    inactiveZone(x, y, fleet_plr, ship)
    # если построена последняя палуба корабля
    if len(ship) == sum_deck:
        ship.sort()
        aroundShip(ship, fleet_plr)
        return ship_plr, str(ind[ship_plr.index(ship)+1]), True
    '''for i in ship_plr:
        print(i)
    print('выход с plr_check')
    for i in fleet_plr:
        print(i)
    print('-'*30)'''
    return ship_plr, str(sum_deck), True

# деактивация кнопок-ячеек, куда нельзя ставить палубу
def inactiveZone(x, y, fleet_plr, ship):
    # если строится первая палуба
    print('-'*30)
    if len(ship) == 1:
        # проверка 3-х палубного на достаточность места
        possible = [[x-1,y], [x,y+1], [x+1,y], [x,y-1]]
        for i in range(10):
            for j in range(10):
                if ([i,j] not in possible and
                    fleet_plr[i][j] != 3 and
                    fleet_plr[i][j] != 6):
                    fleet_plr[i][j] = 5
    elif len(ship) >= 2:
        # проверка на линейность
        if x == ship[0][0]:
            min_y, max_y = m_Y(ship)
            possible = [[x, min_y], [x, max_y]]
        elif y == ship[0][1]:
            min_x, max_x = m_X(ship)
            possible = [[min_x, y], [max_x, y]]
        for i in range(10):
            for j in range(10):
                if ([i,j] not in possible and
                    fleet_plr[i][j] != 3 and
                    fleet_plr[i][j] != 6):
                    fleet_plr[i][j] = 5
    # размещение палубы в ячейке
    fleet_plr[x][y] = 3
    '''print('-'*30)
    print('выход с inactive_zone')
    for i in fleet_plr:
        print(i)
    print('-'*30)'''

# вычисление мёртвых зон, куда не станет корабль
def deadZone(x, y, ship, ship_plr, fleet_plr, sum_deck=3):
    print('вход в dead_zone => [',x,'][',y,']','=',fleet_plr[x][y])
    if fleet_plr[x][y] == 0:
        j, z = 0, []
        virt_ship_x = []
        virt_ship_y = []
        # возможности размещения корабля
        for k in [x, y]:
            for i in range(k-(sum_deck-1), k+sum_deck):
                if 9>=i>=0:
                    if j == 0:
                        if (fleet_plr[i][y] == 0 or
                            fleet_plr[i][y] == 5):
                            virt_ship_x.append([i,y])
                    elif j == 1:
                        if (fleet_plr[x][i] == 0 or
                            fleet_plr[x][i] == 5):
                            virt_ship_y.append([x,i])
            j += 1
        for virt_ship in [virt_ship_x, virt_ship_y]:
            z.append(checkVirtShip(x, y, ship, virt_ship,
                                     ship_plr, fleet_plr))
        if True in z:
            return True
    else:
        print('-'*10)
        return False

def m_X(ship):
    x_x = []
    for deck in ship:
        x_x.append(deck[0])
    return min(x_x)-1, max(x_x)+1

def m_Y(ship):
    y_y = []
    for deck in ship:
        y_y.append(deck[1])
    return min(y_y)-1, max(y_y)+1

# очерчевание целого корабля неактивной зоной
def aroundShip(ship, fleet_plr):
    for deck in ship:
        x, y = deck[0], deck[1]
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if 9>=i>=0 and 9>=j>=0:
                    if (fleet_plr[i][j]==0 or
                        fleet_plr[i][j]==5):
                        fleet_plr[i][j]=6
    # активация ячеек для постоения следующего корабля
    for i in range(10):
        for j in range(10):
            if fleet_plr[i][j] == 5:
                fleet_plr[i][j] = 0
    print('КОРАБЛЬ ПОСТРОЕН ПОЛНОСТЬЮ!')

# деактивация ячеек в мёртвых зонах
def checkVirtShip(x, y, ship, virt_ship, ship_plr, fleet_plr):
    print('k, virt_ship в dead_zone =>', virt_ship)
    sum_deck = ind[ship_plr.index(ship)]
    if (len(ship) == 0 and
        len(virt_ship) > (sum_deck-1)):
        print('разрешается по ПЕРВОМУ условию')
        print('-'*10)
        return True
    # если строится 2 палуба 2-х или 3-х палубного
    elif (len(ship) > 0 and
          len(virt_ship) >= 1):
        print('разрешается по ВТОРОМУ условию')
        print('-'*10)
        return True
    else:
        # деактивация ячейки, куда не влезет корабль
        virt_ship.remove([x, y])
        print('удаляется virt_ship',virt_ship)
        for deck in virt_ship:
            fleet_plr[deck[0]][deck[1]] = 5
        return False
