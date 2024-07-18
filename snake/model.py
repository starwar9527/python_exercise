import os.path

import torch
import torch.nn as nn
import torch.nn.functional as F


class Model(nn.Module):
    def __init__(self, input_layer, hidden_layer, output_layer):
        super().__init__()
        self.linear1 = nn.Linear(input_layer, hidden_layer)
        self.linear2 = nn.Linear(hidden_layer, output_layer)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x

    def save(self, file_name='model.pth'):
        folder = './Model'
        if not os.path.exists(folder):
            os.makedirs(folder)
        full_name = os.path.join(folder, file_name)
        self.save(self.state_dict(), full_name)


class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = torch.optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_one_step(self, state, action, reward, next_state, done):
        # (n, x)
        state = torch.tensor(state)
        action = torch.tensor(action)
        reward = torch.tensor(reward)
        next_state = torch.tensor(next_state)
        done = torch.tensor(done)

        # (1, x)
        if len(done.shape) == 1:
            state = state.squeeze(0)
            action = action.squeeze(0)
            reward = reward.squeeze(0)
            next_state = next_state.squeeze(0)
            done = (done,)

        # predicted Q value with current state
        pred = self.model(state)

        # Q_new = r + y * max(next_prediction Q value) -> only do this if not done, otherwise just set to reward
        # pred.clone
        # pred[argmax(action)] = Q_new
        target = pred.clone()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx]:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))

            target[idx][torch.argmax(action).item()] = Q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimizer.step()
