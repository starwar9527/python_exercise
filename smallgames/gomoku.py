import random


class Gomoku:
    def __init__(self):
        self.row = 15
        self.column = 15
        # user is white
        self.white = 'X'
        # computer is black
        self.black = 'O'
        self.empty_char = '-'
        self.pieces = [self.empty_char] * self.row * self.column

    @staticmethod
    def get_input_pair():
        while True:
            line = input().strip()

            if line.lower() == 'q':
                return 'q', 0
            try:
                a, b = map(int, line.split())
                return a, b
            except ValueError:
                print("Invalid input, please enter two integers separated by space.")

    def play(self):
        self.draw_board()
        while True:
            # get user's move
            print("Please input your position:")
            a, b = self.get_input_pair()
            if a == 'q':
                print('You lose, because you quit.')
                self.draw_board()
                break

            while not self.valid_position(a, b):
                print("Invalid input. Please enter a valid integer.")
                a, b = self.get_input_pair()

            # set user's move
            self.set_piece(a, b, self.white)
            self.draw_board()

            # exits if user wins
            if self.win(a, b, self.white):
                print('You win!')
                self.draw_board()
                break
            elif self.all_filled():
                print('Tie')
                self.draw_board()
                break

            # get computer's move
            cm = random.sample(range(0, self.row), 2)
            while not self.valid_position(cm[0], cm[1]):
                cm = random.sample(range(0, self.row), 2)

            # set computer's move
            self.set_piece(cm[0], cm[1], self.black)

            # exits if computer wins
            if self.win(cm[0], cm[1], self.black):
                print('You lose.')
                self.draw_board()
                break
            elif self.all_filled():
                print('Tie')
                self.draw_board()
                break
            else:
                self.draw_board()

    def draw_board(self):
        # for i in range(225):
        #    if i % 2 == 0:
        #        self.pieces[i] = 'O'
        head = '  '
        for j in range(self.column):
            head += f'{j:2} '
        print(head)

        for i in range(self.row):
            row = self.pieces[i * self.column: (i + 1) * self.column]
            row = f'{i:2} '+'  '.join(row)
            print(row)
        print('\n')

    def assert_valid_position(self, i, j):
        if i < 0 or i > self.row - 1:
            raise ValueError(f"i = {i} is invalid")
        if j < 0 or j > self.column - 1:
            raise ValueError(f"j = {j} is invalid")

    def set_piece(self, i, j, c):
        self.assert_valid_position(i, j)
        self.pieces[i*self.row+j] = c

    def get_piece(self, i, j):
        self.assert_valid_position(i, j)
        return self.pieces[i*self.row+j]

    def win(self, last_i, last_j, c):
        dirs = [[1, 0], [0, 1], [1, 1], [1, -1]]
        for d in dirs:
            if self.win_along_dir(d[0], d[1], last_i, last_j, c):
                return True
        return False

    def win_along_dir(self, dir_x, dir_y, i, j, c):
        last_pos = self.get_last_pos_along_dir(dir_x, dir_y, i, j, c)
        first_pos = self.get_last_pos_along_dir(-dir_x, -dir_y, i, j, c)
        if last_pos + first_pos >= 4:
            return True
        else:
            return False

    def get_last_pos_along_dir(self, dir_x, dir_y, i, j, c):
        self.assert_valid_position(i, j)
        if self.get_piece(i, j) != c:
            raise ValueError(f"piece at ({i}, {j}) is not {c}")

        pos = 0
        x = i + dir_x
        y = j + dir_y

        while 0 <= x < self.row and 0 <= y < self.column and self.get_piece(x, y) == c:
            pos += 1
            x += dir_x
            y += dir_y
        return pos

    def reset_board(self):
        self.pieces = [self.empty_char] * self.row * self.column

    def all_filled(self):
        for i in range(len(self.pieces)):
            if self.pieces[i] == self.empty_char:
                return False
        return True

    def valid_position(self, i, j):
        if 0 <= i < self.row and 0 <= j < self.column and self.get_piece(i, j) == self.empty_char:
            return True
        else:
            return False