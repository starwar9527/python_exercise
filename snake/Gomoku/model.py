import os.path

import torch
import torch.nn as nn
import torch.nn.functional as F


class Model(nn.Module):
    def __init__(self, input_layer, hidden_layer, output_layer):
        super().__init__()
        self.linear1 = nn.Linear(input_layer, hidden_layer)
        self.linear2 = nn.Linear(hidden_layer, output_layer)

        folder = './Model'
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_name = 'model.pth'
        self.model_path = os.path.join(folder, file_name)


    def forward(self, x):
        """
        return the Q_value vector of the state 'x'. the returned value is a vector,
                e.g. if return (9.6, 5.6, 4.3), i.e. for action (1, 0, 0) the Q_value
                is 9.6, for action (0, 1, 0) the Q_value is 5.6, for action (0, 0, 1)
                the Q_value is 4.3
        """
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x

    def save(self, file_name='model.pth'):
        folder = './Model'
        if not os.path.exists(folder):
            os.makedirs(folder)
        full_name = os.path.join(folder, file_name)
        torch.save(self.state_dict(), full_name)

    def read_saved(self):
        # get saved time of the model
        if os.path.exists(self.model_path):
            # Load the state dictionary into the model
            self.load_state_dict(torch.load(self.model_path))
            return True
        return False


class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = torch.optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_one_step(self, state, action, reward, next_state, done):
        # (n, x)
        state = torch.tensor(state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.float)
        reward = torch.tensor(reward, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)

        # (1, x)
        if len(state.shape) == 1:
            state = torch.unsqueeze(state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            next_state = torch.unsqueeze(next_state, 0)
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

            target[idx][torch.argmax(action[idx]).item()] = Q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimizer.step()
