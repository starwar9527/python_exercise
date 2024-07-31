import random


class TicTacToe:
    def __init__(self):
        self.value = [' ']*9
        print(self.value)

    def play(self):
        while True:
            # get user's move
            idx = input('Please input your choice [0,...,8]:')
            while not idx.isnumeric():
                print("Invalid input. Please enter a valid integer.")
                idx = input('Please input your choice [0,...,8]:')
            idx = int(idx)

            while not (idx >= 0 or idx <= 8):
                print("Invalid input. Please enter a valid integer.")
                idx = input('Please input your choice [0,...,8]:')
                idx = int(idx)

            while self.value[idx] != ' ':
                print("Invalid input position. Please enter a valid integer.")
                idx = input('Please input your choice [0,...,8]:')
                idx = int(idx)

            # set user's move
            self.value[idx] = 'X'
            # self.drawboard()

            # exits if user wins
            if self.end('X'):
                print('You win!')
                self.drawboard()
                break
            elif self.all_filled():
                print('Tie')
                self.drawboard()
                break

            # get computer's move
            cidx = random.randrange(9)
            while self.value[cidx] != ' ':
                cidx = random.randrange(9)
            # set computer's move
            self.value[cidx] = 'O'

            # exits if computer wins
            if self.end("O"):
                print('You lose.')
                self.drawboard()
                break
            elif self.all_filled():
                print('Tie')
                self.drawboard()
                break
            else:
                self.drawboard()

    def drawboard(self):
        print(self.value[0], "|", self.value[1], "|", self.value[2])
        print(self.value[3], "|", self.value[4], "|", self.value[5])
        print(self.value[6], "|", self.value[7], "|", self.value[8])

    def end(self, v):
        if (self.value[0] == v and self.value[1] == v and self.value[2] == v or
            self.value[3] == v and self.value[4] == v and self.value[5] == v or
            self.value[6] == v and self.value[7] == v and self.value[8] == v or
            self.value[0] == v and self.value[3] == v and self.value[6] == v or
            self.value[1] == v and self.value[4] == v and self.value[7] == v or
            self.value[2] == v and self.value[5] == v and self.value[8] == v or
            self.value[0] == v and self.value[4] == v and self.value[8] == v or
            self.value[2] == v and self.value[4] == v and self.value[6] == v
        ):
            return True
        return False

    def all_filled(self):
        for i in range(9):
            if self.value[i] == ' ':
                return False
        return True
