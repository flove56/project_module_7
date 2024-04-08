from sklearn.datasets import fetch_openml
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import json
import os
import tensorflow as tf
from keras import models, layers, losses
import cv2
import seaborn as sns

#mode = 'mnist'  # mnist or patch

#if mode == 'mnist':
#    X_mnist, y_mnist = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False, parser='auto')

#    y_mnist = np.array(y_mnist, dtype=int)
#    dim_row = 28
#    dim_col = 28

    # unflatten mnist images
#    X_mnist = np.array([np.reshape(xf, (dim_row, dim_col)) for xf in X_mnist])
#    iters = 2
#else:
dim_row = 27
dim_col = 19
iters = 500

with open(f"{os.path.dirname(os.path.realpath(__file__))}/gestures.json", 'r') as file:
    data = json.load(file)
#the frames
X_data = np.array([d["frame"] for d in data])
#the labels
#dictkey = {'t': "petting", 'k': "poking", 'c': "comforting", 'h': "hitting", 's': "scratching"}
dictkey = {'petting': 1, 'poking': 2, 'comforting': 3, 'hitting': 4, 'scratching': 5}
y_data = np.array([dictkey[d["label"]] for d in data])
print(y_data)



def plot_digits(X, y):
    plt.figure(figsize=(20, 6))
    for i in range(10):
        if np.where(y == f"{i}")[0].size > 0:
            index = np.where(y == f"{i}")[0][0]
            digit_sub = plt.subplot(2, 5, i + 1)
            digit_sub.imshow(np.reshape(X[index], (dim_row, dim_col)), cmap="gray")
            digit_sub.set_xlabel(f"Digit {y[index]}")
    plt.show()


#if mode == 'mnist':
#    X_train, X_test, y_train, y_test = train_test_split(X_mnist, y_mnist, test_size=0.25)
#else:
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.25)

model = models.Sequential()
model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(dim_row, dim_col, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.compile(optimizer='adam',
              loss=losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

hist = model.fit(X_train, y_train, epochs=iters, validation_split=0.2)
plt.plot(hist.history['accuracy'], label='accuracy')
plt.plot(hist.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

y_pred = model.predict(X_test)
print(y_pred)
y_pred = np.argmax(y_pred, axis=1)
print(y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
# plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title('Confusion Matrix for Decision Tree')
plt.show()

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"Test loss: {test_loss} Test accuracy: {test_acc}")


