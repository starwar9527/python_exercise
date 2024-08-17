from StonePaperScissor import stone_paper_scissor
from tictactoe import TicTacToe

while True:
    text = """Please select one of the games (press a number or 'q' to quit):
               1. Guess
               2. StonePaperScissor
               3. Straight4
               4. Worble
               5. TicTacToe \n"""
    id = input(text)
    if id == '1':
        print('Guess selected')
    elif id == '2':
        print('2 selected')
        stone_paper_scissor()
    elif id == '3':
        print('3')
    elif id == '4':
        print('4')
    elif id == '5':
        game = TicTacToe()
        game.play()
    elif id == 'q':
        break

