#!/usr/bin/env python3

import tensorflow as tf

print("TensorFlow version::", tf.__version__)

# Load a dataset

mnist = tf.keras.datasets.mnist

# Preload a dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0, x_test/255.0

# build a machine learning model:
# build a tf.keras.Sequential

# Sequential is useful for stacking layers where each layer has one input tensor and one output tensor
# Layers are functions with known mathematical strucure that can be used and have trainable variables

# Model uses -: Flatten, Dense and Dropout layers
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

# returns a vector of logits or logodds scores one for each class
predictions = model(x_train[:1]).numpy()
predictions

print('predictions::', predictions)

print('probabilities::', tf.nn.softmax(predictions).numpy())

# loss_fn: for training the model
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# Before training, compile the models using th loss_fn function from above

model.compile(
  optimizer='adam',
  loss=loss_fn,
  metrics=['accuracy']
)

# Train and evaluate the model
model.fit(x_train, y_train, epochs=5)

# Evalutate the models performance

model.evaluate(x_test, y_test, verbose=2)