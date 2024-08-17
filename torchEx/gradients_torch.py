import numpy as np
# y = w*x, for w = 2

a = np.array([1, 2, 3, 4, 5], dtype=np.float32)
b = np.array([2, 4, 6, 8, 10], dtype=np.float32)
w = 0
iter = 10
learning_rate = 0.01

def predict(x):
    return w * x

# MSE
def loss(y_p, y):
    return ((y_p-y)**2).mean()

# loss gradient with respect to weight
# 1/N * 2 *(w*x - y)*x
def grad(x, y_p, y):
    return np.dot(2.0*(y_p-y), x).mean()

test = 6
print(f'test before training is {predict(test)}')

# training
for epoch in range(iter):
    y_p = predict(a)
    l = loss(y_p, b)
    w -= learning_rate*grad(a, y_p, b)
    print(f'epoch {epoch}, with loss {l:.3f}, weight {w:.5f}, test is {predict(test):.5f}')
    #print(f'epoch {epoch}, with loss {l:.8f}, weight {w:.5f}')
