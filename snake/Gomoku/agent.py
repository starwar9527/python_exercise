import random

import numpy as np
import torch

from Gomoku.gomoku import Gomoku
from Gomoku.model import Model, QTrainer
from collections import deque
from helper import plot

MAXLEN = 100_000
BATCH_SIZE = 1000
LR = 0.001
DIM = 225

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0.9  # discount rate
        self.memory = deque(maxlen=MAXLEN)  # popleft() is called when max arrived
        self.model = Model(DIM, 256, DIM)   # dim for state space is 225, action space also 225
        self.trainer = QTrainer(self.model, LR, self.gamma)

    def get_state(self, game):
        state = game.get_state()
        return np.array(state, dtype=int)

    def get_move(self, state, loaded=False):
        # random move: tradeoff exploration/exploitation
        # random move or prediction from model
        final_move = [0] * DIM
        #if not loaded and random.randint(0, 200) < 80 - self.n_games:
        if random.randint(0, 200) < 80 - self.n_games:
            # if the number of games is small, then random
            move = random.randint(0, DIM-1)
            final_move[move] = 1
        else:
            # use model for prediction
            state0 = torch.tensor(state, dtype=torch.float)
            action = self.model(state0)
            move = torch.argmax(action).item()
            final_move[move] = 1
        return final_move

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_one_game_step(self, state, action, reward, next_state, done):
        self.trainer.train_one_step(state, action, reward, next_state, done)

    def train_all_games(self):
        if len(self.memory) > BATCH_SIZE:
            batch = random.sample(self.memory, BATCH_SIZE)
        else:
            batch = self.memory
        states, actions, rewards, next_states, dones = zip(*batch)
        self.trainer.train_one_step(states, actions, rewards, next_states, dones)


def train():
    agent = Agent()
    game = Gomoku()
    loaded = agent.model.read_saved()
    while True:
        old_state = agent.get_state(game)
        move = agent.get_move(old_state, loaded)
        reward, done = game.play_onestep_ai(move)
        new_state = agent.get_state(game)
        agent.remember(old_state, move, reward, new_state, done)

        agent.train_one_game_step(old_state, move, reward, new_state, done)
        if done:
            # train all games
            game.reset_board()
            agent.n_games += 1
            agent.train_all_games()

            # print('Game', agent.n_games, 'Score', score, 'Record:', record)


if __name__ == '__main__':
    train()
