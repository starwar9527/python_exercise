import random


def stone_paper_scissor():
    option = ['stone', 'paper', 'scissor']

    user = input('Please input your choice of stone, paper or scissor:')
    while not user.lower() in option:
        user = input('Wrong input! Please input your choice of stone, paper or scissor:')

    computer = option[random.randrange(3)]
    if computer == user:
        print(f'you have {user}, computer has {computer}, tie')
    elif (computer == option[0] and user == option[2] or
          computer == option[1] and user == option[0] or
          computer == option[2] and user == option[1]):
        print(f'you have {user}, computer has {computer}, you lose')
    else:
        print(f'you have {user}, computer has {computer}, you win!')
