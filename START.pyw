'''главное окно игры'''

import sys
import os
from tkinter import Tk, Frame, Button
from field import (botField, plrField, botPlrBox,
                   statBox, arrange)
from settings import aboutGame

def restartProgram():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def exitProgram():
    root.destroy()

root = Tk()
root.title('Sea Battle')
root.iconbitmap('ship.ico')

root.withdraw()
root.resizable(width=False, height=False)
stat_label = Frame(root, bd=0)              # информационное поле
statBox(stat_label)

bot_box = Frame(root, bd=2, bg='#0094FF')      # поле копьютера
plr_box = Frame(root, bd=2, bg='#0094FF')      # поле игрока
# автоматическая расстановка флота игрока
(state_cell_bot, ship_plr,
 ship_plr_shot, fleet_plr) = arrange(plr_box, bot_box)

root.deiconify()

# игровые поля
info_label = Frame(root)                    # обозначение полей
botPlrBox(info_label)

plrField(plr_box, bot_box, ship_plr, ship_plr_shot, fleet_plr)

botField(bot_box, plr_box, state_cell_bot,
          ship_plr, ship_plr_shot, fleet_plr)

# расстановка полей
info_label.grid(row=0, column=0, columnspan=3)
bot_box.grid(row=1, column=0)
stat_label.grid(row=1, column=1)
plr_box.grid(row=1, column=2)

# нижнее меню - футер
n_game = Frame(root, bd=5)
new = Button(n_game, text="Новая Игра", command=restartProgram)
new.config(bg='silver')
new.grid(row=0, column=0)
n_game.grid(row=2, column=0)

a_game = Frame(root, bd=5)
about = Button(a_game, text="Справка", command=lambda:aboutGame())
about.config(bg='silver')
about.grid(row=0, column=0)
a_game.grid(row=2, column=1)

e_game = Frame(root, bd=5)
exit_game = Button(e_game, text="Выход", command=exitProgram)
exit_game.config(bg='silver')
exit_game.grid(row=0, column=1)
e_game.grid(row=2, column=2)

root.mainloop()
