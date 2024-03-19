class Pawn:
    def __init__(self, color):
        self.color = color
        self.first_move = True

    def __str__(self):
        return ('♙', '♟')[self.color]

    def can_move(self, stand: str, move: str, table):
        move_num = int(move[1])
        stand_num = int(stand[1])
        vert = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1, 'h': 0}

        if 1 < move_num < 8 and move_num in [stand_num+1, stand_num+2 if self.first_move else stand_num+1]:
            if move[0] in vert.keys():
                if move[0] == stand[0]:
                    if self.first_move and move_num == stand_num + 2:
                        if table.table[vert[move[0]]][move_num] == 0:
                            return [True]
                        else:
                            return [False, 'Нельзя перепрыгнуть через фигуру']
                else:
                    if move[0] in ('abcdefgh'[vert[move[0]]], 'abcdefgh'[vert[move[0]] + 2]):
                        if table.table[vert[move[0]]][move_num] != 0:
                            return [True]
                    else:
                        return [False, 'Ты даун?']


print()

