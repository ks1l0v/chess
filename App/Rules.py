def check_move(move: str, table):
    if move[1].isdigit() and 0 < int(move[1]) < 9:
        entity = table['abcdefgh'.index(move[0])][int(move[1]) - 1]
        if isinstance(entity, int):
            return False
        else:
            return entity
    else:
        return False


def check_position(turn_color: int, move):
    if move != 0:
        if move.color != turn_color:
            return [True]
        else:
            return [False, 'Нельзя съесть свою фигуру']
    else:
        return True


def move_figure(move_from, move_to, table):
    entity = ['abcdefgh'.index(move_from[0])][int(move_from[1]) - 1]
    table['abcdefgh'.index(move_from[0])][int(move_from[1]) - 1] = 0
    table['abcdefgh'.index(move_to[0])][int(move_to[1]) - 1] = entity