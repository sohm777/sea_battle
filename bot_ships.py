'''автоматическая расстановка кораблей на поле'''

from four_deck_ship import four
from three_deck_ship import three
from two_deck_ship import two
from one_deck_ship import one

def botFleet():
    # создание или обнуление игрового поля
    fleet_null = [ [0 for j in range(10)] for i in range(10)]
    # строится один 4-палубный
    ship_four, fleet_four = four(fleet_null)
    # строятся два 3-палубных
    ship_three_1, fleet_three = three(fleet_four)
    ship_three_2, fleet_three = three(fleet_three)
    # строятся три 2-палубных
    ship_two_1, fleet_two = two(fleet_three)
    ship_two_2, fleet_two = two(fleet_two)
    ship_two_3, fleet_two = two(fleet_two)
    # строятся четыре 1-палубных
    ship_one_1, fleet_one = one(fleet_two)
    ship_one_2, fleet_one = one(fleet_one)
    ship_one_3, fleet_one = one(fleet_one)
    ship_one_4, fleet_one = one(fleet_one)
    ships = (ship_four, ship_three_1, ship_three_2,
             ship_two_1, ship_two_2, ship_two_3,
             ship_one_1, ship_one_2,
             ship_one_3, ship_one_4)
    for i in ships:
        print(i)
    print('-'*30)
    return ships, fleet_one
