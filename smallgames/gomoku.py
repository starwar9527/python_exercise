class Gomoku:
    def __init__(self):
        self.row = 15
        self.column = 15
        self.pieces = [''] * self.row * self.column

    def play(self):
        pass

    def draw_pieces(self):
        for i in range(self.row):
            row = self.pieces[row * self.column: (row + 1) * self.column]
            row = ''.join(row)
            print(row)

    def set_piece(self, i, j, c):
        if i < 0 or i > self.row - 1:
            raise ValueError(f"i = {i} is invalid")
        if j < 0 or j > self.column - 1:
            raise ValueError(f"j = {j} is invalid")
        self.pieces[i*self.row+j] = c

    def get_piece(self, i, j):
        if i < 0 or i > self.row - 1:
            raise ValueError(f"i = {i} is invalid")
        if j < 0 or j > self.column - 1:
            raise ValueError(f"j = {j} is invalid")
        return self.pieces[i*self.row+j]
