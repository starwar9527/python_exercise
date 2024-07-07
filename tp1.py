import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

#print(tf.__version__)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# read in data
data = keras.datasets.fashion_mnist

# split data
(train_data, train_labels), (test_data, test_labels) = data.load_data()

# show data
#print(len(train_data))

train_data = train_data/256.0
test_data = test_data/256.0

#print(train_data[7])

plt.figure(figsize = (10, 10))
for i in range(25):
	plt.subplot(5, 5, i+1)
	plt.xticks([])
	plt.yticks([])
	#plt.grid(False)
	plt.imshow(train_data[i])
	plt.xlabel(class_names[train_labels[i]])
#plt.show()

#build model
model = tf.keras.models.Sequential([
	tf.keras.layers.Flatten(input_shape=(28, 28)),
	tf.keras.layers.Dense(128, activation='relu'),
	tf.keras.layers.Dropout(0.2),
	tf.keras.layers.Dense(10)
])

prediction = model(train_data[:1]).numpy()
#print(tf.nn.softmax(prediction).numpy())
loss_fn = tf.keras.losses.sparse_categorical_crossentropy(from_logits=True)

print(loss_fn(train_labels[:1], prediction))

#train_model

#test_model


