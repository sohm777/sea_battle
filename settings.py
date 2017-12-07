'''файл настроек игры'''

from tkinter.messagebox import askyesno, showinfo
from bot_ships import botFleet

# цвета кнопок (ячеек)
colors = {'0':'#9AFFFF',   # пустое поле - акт
          '1':'grey',   # промах, очерчевание корабля, не акт
          '2':'#FF3C47',    # попадание
          '3':'#2d2d2d',  # поле живого корабля(палубы) игрока
          '4':'silver', # не активная пустая ячейка
          '5':'#9AFFFF',   # не активная пустая ячейка для постоения
          '6':'#9AFFFF',   # не акт пустая ячейка для очерчивания
          '7':'#9AFFFF'}   # не акт, мёртвые зоны
        
info = {'0':'Расставьте\nфлот',
        '1':'Стреляйте!',
        '2':'Противник\nстреляет!',
        '3':'ПОБЕДА !!!',
        '4':'Вы ПРОИГРАЛИ'}

shot_info = {'0':'May the Force\nbe with you',
             '1':'Вы промазали',
             '2':'Вы уничтожили\nкорпус!',
             '3':'Корабль\nпотоплен!!',
             '4':'GAME\nOVER'}

hint_info = {'0':'НЕВОЗМОЖНО\nразместить\nпалубу\nв данном месте',
             '1':'Расположите\nОДНО\nпалубный\nкорабль',
             '2':'Расположите\nДВУ\nпалубный\nкорабль',
             '3':'Расположите\nТРЁХ\nпалубный\nкорабль',
             '4':'Расположите\nЧЕТЫРЁХ\nпалубный\nкорабль',
             '5':'В бой!',
             '6':'Hasta la vista,\nbaby!',
             '7':'Идёт бой',
             '8':'Противник\nпромазал',
             '9':'Противник\nуничтожил\nпалубу',
             '10':'Противник\nпотопил\nВаш корабль'}

# видимый флот компа
fleet_bot_visible = [ [0 for j in range(10)]
                      for i in range(10)]

# расставленные корабли и поле компьютера
ships_bot, fleet_bot = botFleet()

# оставшиеся после попаданий корабли компа
ships_bot_shot = []
for ship in (ships_bot):
    ships_bot_shot.append(list(ship))

# авт.расстановка кораблей и корректировка поля игрока
def adjustment():
    # авт. расстановка кораблей игрока
    ship_plr, fleet_plr = botFleet()
    for i in range(10):
        for j in range(10):
            if fleet_plr[i][j] == 1 or fleet_plr[i][j] == 0:
                fleet_plr[i][j] = 5
            elif fleet_plr[i][j] == 2:
                fleet_plr[i][j] = 3
                
    # оставшиеся после попаданий корабли игрока
    ship_plr_shot = []
    for ship in (ship_plr):
        ship_plr_shot.append(list(ship))
        
    return ship_plr, ship_plr_shot, fleet_plr

def manualArrange():
    # пустое поле игрока
    fleet_plr = [ [0 for j in range(10)]
              for i in range(10)]

    # пустой флот игрока
    ship_plr = []
    for i in range(10):
        ship_plr.append([])
        
    # оставшиеся после попаданий корабли игрока
    ship_plr_shot = []
    for i in range(10):
        ship_plr_shot.append([])
        
    return ship_plr, ship_plr_shot, fleet_plr

def firstShot(out_shoot = True):
    if askyesno('Ваш выбор','Хотите стрелять первым?'):
        out_shoot = True
        print('outshoot в выборе', out_shoot)
    else:
        out_shoot = False
        print('outshoot в выборе', out_shoot)
    return out_shoot

# функция справки
def aboutGame():
    showinfo('Справка по игре', 'большой текст справки')

def open_file():
    file = 'clearField.txt'
    fleet = [ [0 for j in range(10)] for i in range(10)]
    with open(file) as file:
        for num, line in enumerate(file):
            i = 0
            line = line.rstrip()
            for simb in line:
                fleet[num][i] = int(simb)
                i += 1
    return fleet
