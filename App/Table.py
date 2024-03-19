from Figures import *


class Table:
    def __init__(self):
        self.table = [[0] * 8 for _ in range(8)]
        self.table[1] = [Pawn(0) for _ in range(8)]
        self.table[6] = [Pawn(1) for _ in range(8)]

    def __str__(self):
        final_table = ''
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if self.table[i][j] != 0:
                    final_table += f'{self.table[i][j]} '
                else:
                    final_table += f'◼ '
            final_table += '\n'
        return final_table

