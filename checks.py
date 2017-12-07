'''модуль проверки корабля на полное уничтожение
и очерчивание его пустой неактивной областью и
на уничтожение всех кораблей'''

from settings import ships_bot, ships_bot_shot

# очерчивание потопленного корабля неактивной зоной
def inactiveShotArea(ship, fleet_bot_visible):
    for deck in ship:
        x, y = deck[0], deck[1]
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if 9>=i>=0 and 9>=j>=0:
                    if fleet_bot_visible[i][j]==0:
                        fleet_bot_visible[i][j]=1
                        
def checkHit(shot, fleet_bot_visible):
    print('попадание в =>',shot)
    # удаление палубы подбитого корабля
    for num, ship in enumerate(ships_bot_shot):
        if shot in ship:
            ships_bot_shot[num].remove(shot)
            for i in ships_bot_shot:
                print(i)
            if len(ships_bot_shot[num]) == 0:
                inactiveShotArea(ships_bot[num],
                                   fleet_bot_visible)
                return True

def checkEnd():
    deck_len = True
    for ship in ships_bot_shot:
        if len(ship) != 0:
            deck_len = False
    return deck_len
