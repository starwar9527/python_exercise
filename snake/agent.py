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
        self.model = None

    def get_state(self, game):
        pass

    def get_move(self, state):
        pass

    def remember(self, state, reward, score, done):
        pass

    def train_one_game_step(self, state, reward, score, done):
        pass

    def train_all_games(self):
        pass


def train():
    agent = Agent()
    game = Game()
    old_state = agent.get_state(game)
    move = agent.get_move(old_state)
    reward, score, done = game.play_step(move)
    new_state = agent.get_state(game)
    agent.remember(old_state, reward, score, done)

    agent.train_one_game_step(old_state, reward, score, done)
    if done:
        agent.n_games += 1
        agent.train_all_games()

if __name__ == '__main__':
    train()
