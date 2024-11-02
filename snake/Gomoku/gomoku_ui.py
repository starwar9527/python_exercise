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

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Gomoku")

# Draw the board grid
def draw_board():
    screen.fill(BG_COLOR)
    for row in range(BOARD_SIZE):
        # Draw horizontal lines
        pygame.draw.line(
            screen, LINE_COLOR,
            (MARGIN, MARGIN + row * CELL_SIZE),
            (MARGIN + (BOARD_SIZE - 1) * CELL_SIZE, MARGIN + row * CELL_SIZE),
            1
        )
        # Draw vertical lines
        pygame.draw.line(
            screen, LINE_COLOR,
            (MARGIN + row * CELL_SIZE, MARGIN),
            (MARGIN + row * CELL_SIZE, MARGIN + (BOARD_SIZE - 1) * CELL_SIZE),
            1
        )

# Draw a stone on the board
def draw_stone(row, col, color):
    x = MARGIN + col * CELL_SIZE
    y = MARGIN + row * CELL_SIZE
    pygame.draw.circle(screen, color, (x, y), CELL_SIZE // 2 - 2)

# Main game loop
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]  # Empty board
current_player = 1  # 1 for black, -1 for white

while True:
    draw_board()

    # Draw stones from the board state
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 1:
                draw_stone(row, col, BLACK_COLOR)
            elif board[row][col] == -1:
                draw_stone(row, col, WHITE_COLOR)

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
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == 0:
                board[row][col] = current_player
                current_player *= -1  # Switch player

    pygame.display.flip()
