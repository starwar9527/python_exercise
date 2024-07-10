from game import Game
from model import Model
from collections import deque
import os

MAXLEN = 100_000

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0
        self.memory = deque(maxlen=MAXLEN)
        self.game = None
        self.model = None

    def get_state(self):
        pass

    def get_move(self):
        pass

    def remember(self):
        pass

    def train_one_game_step(self):
        pass

    def train_all_games(self):
        pass


def train():
    pass


if __name__ == '__main__':
    train()
    