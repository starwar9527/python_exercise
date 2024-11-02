import random
import pygame
import sys

# Initialize constants
BOARD_SIZE = 15           # 15x15 board
CELL_SIZE = 40            # Size of each cell in pixels
MARGIN = 20               # Margin around the board
WINDOW_SIZE = BOARD_SIZE * CELL_SIZE + MARGIN * 2

# Colors
BG_COLOR = (230, 200, 150)  # Background color of the board
LINE_COLOR = (0, 0, 0)      # Color of grid lines
BLACK_COLOR = (0, 0, 0)     # Color of black pieces
WHITE_COLOR = (255, 255, 255) # Color of white pieces
TEXT_COLOR = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Fonts
font = pygame.font.SysFont(None, 48)

class Gomoku:
    def __init__(self):
        self.row = BOARD_SIZE
        self.column = BOARD_SIZE
        # user is white
        self.white = 'X'
        # computer is black
        self.black = 'O'
        self.empty_char = '-'
        self.pieces = [self.empty_char] * self.row * self.column
        # two players, 1 or -1. 1 for black, -1 for white
        self.current_player = 1

        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Gomoku")

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

    def play_step(self):
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

    def get_color(self):
        if self.current_player == 1:
            return self.black
        elif self.current_player == -1:
            return self.white
        else:
            raise ValueError(f"current_player is {self.current_player}, not valid")

    # Function to display the winning mess
    # age
    def show_winner_message(self, winner):
        # Create the winning text surface
        text = f"{winner} wins!"
        text_surface = font.render(text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

        # Draw a rectangle "popup" background behind the text
        pygame.draw.rect(self.screen, (255, 255, 255), text_rect.inflate(20, 20))  # White rectangle background
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()

        # Pause for a moment to show the message
        pygame.time.delay(2000)  # Display for 2 seconds

    def play(self):
        while True:
            game_end = False
            self.draw_board()
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Convert mouse position to board row/col
                    x, y = event.pos
                    col = (x - MARGIN + CELL_SIZE // 2) // CELL_SIZE
                    row = (y - MARGIN + CELL_SIZE // 2) // CELL_SIZE

                    # Make sure it's a valid board position and the cell is empty
                    #if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == 0:
                    if self.valid_position(row, col):
                        self.set_piece(row, col, self.get_color())
                        self.draw_board()
                        winner = 'Black'
                        if self.win(row, col, self.get_color()):
                            if self.current_player == 1:
                                print('Black win!')
                            elif self.current_player == -1:
                                print('White win!')
                                winner = 'White'
                            game_end = True
                        elif self.all_filled():
                            print('Tie')
                            game_end = True
                        if game_end:
                            self.show_winner_message(winner)
                            pygame.quit()
                            sys.exit()

                        self.current_player *= -1  # Switch player

            pygame.display.flip()

    def draw_board(self):
        self.screen.fill(BG_COLOR)
        for row in range(BOARD_SIZE):
            # Draw horizontal lines
            pygame.draw.line(
                self.screen, LINE_COLOR,
                (MARGIN, MARGIN + row * CELL_SIZE),
                (MARGIN + (BOARD_SIZE - 1) * CELL_SIZE, MARGIN + row * CELL_SIZE),
                1
            )
            # Draw vertical lines
            pygame.draw.line(
                self.screen, LINE_COLOR,
                (MARGIN + row * CELL_SIZE, MARGIN),
                (MARGIN + row * CELL_SIZE, MARGIN + (BOARD_SIZE - 1) * CELL_SIZE),
                1
            )
            # Draw stones from the board state
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    ind = row * BOARD_SIZE + col
                    if self.pieces[ind] == self.black:
                        self.draw_stone(row, col, BLACK_COLOR)
                    elif self.pieces[ind] == self.white:
                        self.draw_stone(row, col, WHITE_COLOR)


    # Draw a stone on the board
    def draw_stone(self, row, col, color):
        x = MARGIN + col * CELL_SIZE
        y = MARGIN + row * CELL_SIZE
        pygame.draw.circle(self.screen, color, (x, y), CELL_SIZE // 2 - 2)

    def draw_board_c(self):
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


if __name__ == '__main__':
    game = Gomoku()
    # game.draw_pieces()
    game.play()