from Table import *
from Rules import check_position, check_move, move_figure


def main():
    turn_color = 0
    table = Table()

    while True:
        print(table)
        move_from = check_move(input('from - '), table.table)
        if move_from:
            move_to = input('to - ')
            if check_position(turn_color, move_to):
                move_figure(move_from, move_to, table)
                print(table)
        else:
            print('Далбаеб там пусто')


if __name__ == '__main__':
    main()