'''создание одной кнопки-ячейки'''
from tkinter import *
import time
import random
from tkinter.messagebox import askyesno
from settings import (info, shot_info, hint_info, colors,
                      fleet_bot, fleet_bot_visible,
                      adjustment, manualArrange, firstShot)
from checks import checkHit, checkEnd
from plr_ships import checkDeadZone
from bot_ships import botFleet
from bot_shooting import botShot

# создаёт фрейм для кнопок-ячеек на поле компьютера
def botField(parent_bot, parent_plr, state_cell_bot,
             ship_plr, ship_plr_shot,
             fleet_plr, state_cell=NORMAL):
    for x in range(10):
        for y in range(10):
            if state_cell_bot == DISABLED:
                state_cell = DISABLED
            elif (fleet_bot_visible[x][y] == 1 or
                fleet_bot_visible[x][y] == 2):
                state_cell = DISABLED
            else:
                state_cell = NORMAL
            oneBotBtn(parent_bot, x, y, state_cell,
                      str(fleet_bot_visible[x][y]),
                      ship_plr, ship_plr_shot,
                      fleet_plr, parent_plr)

# построение одной ячейки на поле компьютера
def oneBotBtn(parent_bot, x, y, state_cell, color,
              ship_plr, ship_plr_shot, fleet_plr, parent_plr):
    frame = Frame(parent_bot)
    btn = Button(frame, width=3, height=1)
    if fleet_bot_visible[x][y] == 2 and state_cell == DISABLED:
        btn.config(cursor='pirate')
    elif state_cell == DISABLED:
        btn.config(cursor='X_cursor')
    else:
        btn.config(cursor='cross')
    btn.config(bg=colors[color])
    # состояние данной кнопки
    btn.config(state=state_cell)
    # выстрел по боту
    btn.config(command=lambda:clicksBotBtn(parent_bot, btn,
                                           x, y,
                                           ship_plr, ship_plr_shot,
                                           fleet_plr, parent_plr))
    btn.grid()
    frame.grid(row=x, column=y)

# действие клика по кнопке-ячейке на поле компьютера (выстрел игрока)
def clicksBotBtn(parent_bot, btn, x, y,
                 ship_plr, ship_plr_shot, fleet_plr,
                 parent_plr):
    # метка-hint пустая
    hint_text.set(hint_info['7'])
    # если игрок промазал
    if fleet_bot[x][y] == 0 or fleet_bot[x][y] == 1:
        print('ИГРОК промах в =>', [x, y])
        btn.config(bg=colors['1'], state=DISABLED, cursor='X_cursor')
        fleet_bot_visible[x][y] = 1
        shot_text.set(shot_info['1'])
        '''выстрел компьютера'''
        # метка - противник стреляет
        info_text.set(info['2'])
        (x_p, y_p, ship_plr,
         ship_plr_shot,
         fleet_plr, shooted,
         dead, end) = botShot(ship_plr, ship_plr_shot, fleet_plr)
        # перерисовка поля игрока после выстрела компа
        if shooted or dead:
            plrField(parent_plr, parent_bot,
                     ship_plr, ship_plr_shot,
                     fleet_plr, DISABLED)
            if shooted:
                # метка - стреляйте
                info_text.set(info['1'])
                # метка - противник уничтожил палубу
                hint_text.set(hint_info['9'])
            if dead:
                # метка - противник потопил
                hint_text.set(hint_info['10'])
            if end:
                # метка - вы проиграли
                info_text.set(info['4'])
                # метка - game over
                shot_text.set(shot_info['4'])
                # метка - Hasta la vista
                hint_text.set(hint_info['6'])
                # деактикация поля компьютера
                botField(parent_bot, parent_plr, DISABLED,
                         ship_plr, ship_plr_shot, fleet_plr)
        else:
            # метка - стреляйте
            info_text.set(info['1'])
            # метка - противник промазал
            hint_text.set(hint_info['8'])
            # перерисовка одной ячейки
            onePlrBtn(parent_plr, parent_bot, x_p, y_p, DISABLED,
                      str(fleet_plr[x_p][y_p]),
                      ship_plr, ship_plr_shot, fleet_plr)
        
    # если игрок попал в палубу
    elif fleet_bot[x][y] == 2:
        print('ИГРОК попал в =>', [x, y])
        btn.config(bg=colors['2'], state=DISABLED, cursor='pirate')
        fleet_bot_visible[x][y] = 2
        # проверка попадания на затопление корабля
        if checkHit([x, y], fleet_bot_visible):
            # конец игры?
            if checkEnd():
                for i in range(10):
                    for j in range(10):
                        if fleet_bot_visible[i][j] == 0:
                            fleet_bot_visible[i][j] = 1
                # метка - победа
                info_text.set(info['3'])
                # метка - game over
                shot_text.set(shot_info['4'])
                # метка - Hasta la vista
                hint_text.set(hint_info['6'])
            else:
                # метка - стреляйте
                info_text.set(info['1'])
            # перерисовка поля компа с очерченой зоной
            botField(parent_bot, parent_plr, NORMAL,
                     ship_plr, ship_plr_shot, fleet_plr)
            # метка - потопил
            shot_text.set(shot_info['3'])
        else:
            # метка - уничтожил корпус
            shot_text.set(shot_info['2'])

# выбор возможности расстановка флота игрока
def arrange(parent_plr, parent_bot):
    if askyesno('Добро пожаловать в Классический морской бой!',
                'Расставить Ваш флот автоматически?'):
        
        # корректировка флота игрока
        ship_plr, ship_plr_shot, fleet_plr = adjustment()
        
        # перерисовка поля игрока с автомат.расставленными кораблями
        plrField(parent_plr, parent_bot, ship_plr,
                 ship_plr_shot, fleet_plr, DISABLED)

        # активация поля компьютера
        state_cell_bot = NORMAL
        # метка - стреляйте
        info_text.set(info['1'])
        # метка - в бой
        hint_text.set(hint_info['5'])
    else:
        # деактивация поля комп. на время расс-ки кораблей игроком
        state_cell_bot = DISABLED
        ship_plr, ship_plr_shot, fleet_plr = manualArrange()
        
    return state_cell_bot, ship_plr, ship_plr_shot, fleet_plr

# создаёт фрейм для кнопок на поле игрка
def plrField(parent_plr, parent_bot, ship_plr, ship_plr_shot,
             fleet_plr, state_cell=NORMAL):
    
    for x in range(10):
        for y in range(10):
            if fleet_plr[x][y] == 0:
                state_cell = NORMAL
            else:
                state_cell = DISABLED
            onePlrBtn(parent_plr, parent_bot, x, y, state_cell,
                      str(fleet_plr[x][y]), ship_plr,
                      ship_plr_shot, fleet_plr)

# построение одной яейки на поле игрока
def onePlrBtn(parent_plr, parent_bot, x, y, state_cell, color,
              ship_plr, ship_plr_shot, fleet_plr):
    frame = Frame(parent_plr)
    btn = Button(frame, width=3, height=1)
    btn.config(bg=colors[color])
    # состояние данной кнопки
    btn.config(state=state_cell)
    if fleet_plr[x][y] == 2 and state_cell == DISABLED:
        btn.config(cursor='pirate')
    elif state_cell == DISABLED:
        btn.config(cursor='X_cursor')
    btn.config(command=lambda:clicksPlr(parent_plr, parent_bot,
                                        btn, x, y, ship_plr,
                                        ship_plr_shot, fleet_plr))
    btn.grid()
    frame.grid(row=x, column=y)

# действие клика по кнопке-ячейке на поле игорка
# расстановка кораблей игроком
def clicksPlr(parent_plr, parent_bot, btn, x, y,
              ship_plr, ship_plr_shot, fleet_plr):
    print('строится в => [',x,'][',y,']')
    ship_plr, sum_deck, permit = checkDeadZone(x, y, ship_plr,
                                               fleet_plr)
    if permit:
        # изменение цвета нажатой кнопки на чёрный
        btn.config(bg=colors[str(fleet_plr[x][y])])
        # изменение текста метки-подсказки
        hint_text.set(hint_info[sum_deck])
        # игрок расставил все корабли - деактивация поля игрока
        if sum_deck == '5':
            # деактивировать поле игрока
            for i in range(10):
                for j in range(10):
                    if fleet_plr[i][j] == 0:
                        fleet_plr[i][j] = 5
            # метка - стреляйте
            info_text.set(info['1'])
            # записать постоенные игроком корабли
            ship_plr_shot = []
            for ship in (ship_plr):
                ship_plr_shot.append(list(ship))
            print('ship_plr_shot',ship_plr_shot)
            # активировать поле компьютера
            state_cell_bot = NORMAL
            botField(parent_bot, parent_plr, state_cell_bot,
                     ship_plr, ship_plr_shot, fleet_plr)
        # перерисовка поля с неактивной зоной
        plrField(parent_plr, parent_bot,
                 ship_plr, ship_plr_shot, fleet_plr)
    else:
        # метка - невозможно установить корабль в данной ячейке
        hint_text.set(hint_info['0'])

# метки - поле противника, поле игрока
def botPlrBox(parent):
    bot = Label(parent, text='поле компьютера')
    bot.config(width=40, font='bold')
    bot.grid(row=0, column=0)
    empty = Label(parent, width=15, relief=GROOVE, bg='#DCDCDC')
    empty.grid(row=0, column=1)
    plr = Label(parent, text='поле игрока')
    plr.config(width=40, font='bold')
    plr.grid(row=0, column=2)

# поля статистики
def infoBox(parent):
    global info_text
    info_text = StringVar()
    inf_stat = Label(parent)
    inf_stat.config(textvariable=info_text, bg='#DCDCDC')
    info_text.set(info['0'])
    inf_stat.config(width=15, height=5, relief=GROOVE)
    inf_stat.grid(row=0, column=0)

def shotBox(parent):
    global shot_text
    shot_text = StringVar()
    shot_stat = Label(parent)
    shot_stat.config(textvariable=shot_text, bg='#DCDCDC')
    shot_text.set(shot_info['0'])
    shot_stat.config(width=15, height=5, relief=GROOVE)
    shot_stat.grid(row=0, column=0)

def hintBox(parent):
    global hint_text
    hint_text = StringVar()
    hint_stat = Label(parent)
    hint_stat.config(textvariable=hint_text, bg='#DCDCDC')
    hint_text.set(hint_info['4'])
    hint_stat.config(width=15, height=7, relief=GROOVE)
    hint_stat.grid(row=0, column=0)

# расстановка меток статистики
def statBox(parent):
    info = Frame(parent)
    infoBox(info)
    shot = Frame(parent)
    shotBox(shot)
    hint = Frame(parent)
    hintBox(hint)
    info.grid(row=0, column=0)
    shot.grid(row=1, column=0)
    hint.grid(row=2, column=0)
