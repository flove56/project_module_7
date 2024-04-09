from sklearn.datasets import fetch_openml
from sklearn.dummy import DummyClassifier
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
from keras.models import load_model

dim_row = 27
dim_col = 19
iters = 16

with open(f"{os.path.dirname(os.path.realpath(__file__))}/gesturesfemke.json", 'r') as file:
    data = json.load(file)
#the frames
X_data = np.array([d["frame"] for d in data])
#the labels
#dictkey = {'t': "petting", 'k': "poking", 'c': "comforting", 'h': "hitting", 's': "scratching"}
dictkey = {'petting': 0, 'poking': 1, 'comforting': 2, 'hitting': 3, 'scratching': 4}
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


X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.25)
#first model that acutally works standing still
'''model = models.Sequential()
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
#graph to show the accuracy of the model

hist = model.fit(X_train, y_train, epochs=iters, validation_split=0.2)
plt.plot(hist.history['accuracy'], label='accuracy')
plt.plot(hist.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()
'''

batch_size = 8
def drop_remain(X,y):
    remain = X.__len__() % batch_size
    if remain == 0:
        return X, y
    else:
        X = X[:-remain, :,:]
        y = y[:-remain]
        return X, y
X_train, y_train = drop_remain(X_train, y_train)
X_test, y_test = drop_remain(X_test, y_test)
#X_val, y_val = drop_remain(X_val, y_val)

model = models.Sequential()
model.add(layers.LSTM(64, stateful=True, return_sequences=True))
model.add(layers.LSTM(64, stateful=True, return_sequences=True))
model.add(layers.LSTM(64, stateful=True))
model.add(layers.Dense(10))




model.compile(optimizer='adam',
              loss=losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
hist = {'loss':[],'accuracy':[]}
#hist = {'loss':[],'accuracy':[],'val_loss':[],'val_accuracy':[]}
for i in range(iters):
    epoch_hist = model.fit(X_train,y_train, epochs=1, batch_size=batch_size, verbose=2, shuffle=False)
    for key in hist.keys():
        hist[key].append(epoch_hist.history[key])

    for layer in model.layers:
        if layer.name == 'lstm':
            layer.reset_states()


#graph to show the accuracy of the model
plt.plot(hist['accuracy'], label='accuracy')
#plt.plot(hist['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()
#model.fit(X_train, y_train, epochs=iters, validation_split=0.2)

#save the model
model.save('model.h5')

test_loss, test_acc = model.evaluate(X_test,  y_test, verbose=2, batch_size=batch_size)
print(test_loss, test_acc)

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


