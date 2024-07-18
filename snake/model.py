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


