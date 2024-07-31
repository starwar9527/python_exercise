from StonePaperScissor import stone_paper_scissor
from tictactoe import TicTacToe

while True:
    id = input('Please select one of the games:\n'
               '1. Guess\n'
               '2. StonePaperScissor\n'
               '3. Straight4\n'
               '4. Worble\n'
               '5. TicTacToe\n')
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
    else:
        print('None of the games is selected, exit')
        break

