import random

import numpy as np
import torch

from game import Game, BLOCK_SIZE, Point, Direction
from model import Model
from collections import deque
import os

MAXLEN = 100_000
BATCH_SIZE = 1000


class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0    # discount rate
        self.memory = deque(maxlen=MAXLEN)  # popleft() is called when max arrived
        self.model = None
        self.trainer = None

    def get_state(self, game):
        pt = game.head
        pt_left = Point(pt.x-BLOCK_SIZE, pt.y)
        pt_right = Point(pt.x+BLOCK_SIZE, pt.y)
        pt_up = Point(pt.x, pt.y-BLOCK_SIZE)
        pt_down = Point(pt.x, pt.y+BLOCK_SIZE)

        dl = game.direction == Direction.LEFT
        dr = game.direction == Direction.RIGHT
        dd = game.direction == Direction.DOWN
        du = game.direction == Direction.UP

        state = [
            # straight danger
            (dl and game.is_collision(pt_left)) or
            (dr and game.is_collision(pt_right)) or
            (dd and game.is_collision(pt_down)) or
            (du and game.is_collision(pt_up)),

            # right danger
            (dl and game.is_collision(pt_up)) or
            (dr and game.is_collision(pt_down)) or
            (dd and game.is_collision(pt_left)) or
            (du and game.is_collision(pt_right)),

            # left danger
            (dl and game.is_collision(pt_down)) or
            (dr and game.is_collision(pt_up)) or
            (dd and game.is_collision(pt_right)) or
            (du and game.is_collision(pt_left)),

            # move direction
            dl,  # left
            dr,  # right
            du,  # up
            dd,  # down

            # food position
            game.food.x < game.head.x,  # left
            game.food.x > game.head.x,  # right
            game.food.y < game.head.y,  # up
            game.food.y > game.head.y   # down
        ]
        return np.array(state, dtype=int)

    def get_move(self, state):
        # random move: tradeoff exploration/exploitation
        # random move or prediction from model
        final_move = [0,0,0]
        if random.randint(0, 200) < 80 - self.n_games:
            # if the number of games is small, then random
            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            # use model for prediction
            state0 = torch.tensor(state, dtype=float)
            action = self.model.predict(state0)
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
    game = Game()
    while True:
        old_state = agent.get_state(game)
        move = agent.get_move(old_state)
        reward, score, done = game.play_step(move)
        new_state = agent.get_state(game)
        agent.remember(old_state, reward, score, done)

        agent.train_one_game_step(old_state, move, reward, new_state, done)
        if done:
            # train all games, plot result
            agent.n_games += 1
            agent.train_all_games()


if __name__ == '__main__':
    train()
