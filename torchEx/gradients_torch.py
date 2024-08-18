import numpy as np
import torch
import torch.nn as nn
# y = w*x, for w = 2

a = torch.tensor([[1], [2], [3], [4]], dtype=torch.float32)
b = torch.tensor([[2], [4], [6], [8]], dtype=torch.float32)

iter = 100
learning_rate = 0.01
n_samples, n_features = a.shape
print(f'{n_samples}, {n_features}')

loss = nn.MSELoss()

model = nn.Linear(in_features = n_features, out_features = n_features)

optimizer = torch.optim.SGD(model.parameters(), lr= learning_rate)

test = torch.tensor([5], dtype=torch.float32)
print(f'test before training is {model(test).item():.3f}')

# training
for epoch in range(iter):
    y_p = model(a)
    #print(f'y_p.shape = {y_p.shape}')
    #print(f'a.shape = {a.shape}')
    #print(f'b.shape = {b.shape}')
    l = loss(y_p, b)
    l.backward()
    optimizer.step()

    optimizer.zero_grad()

    w, _ = model.parameters()

    if epoch % 10 == 0:
        print(f'epoch {epoch}, with loss {l:.3f}, weight {w[0][0].item():.5f}, predict is {model(test).item():.3f}')
        #print(f'epoch {epoch}, with loss {l:.3f}')
        #print(f'epoch {epoch}, with loss {l:.8f}, weight {w:.5f}')
