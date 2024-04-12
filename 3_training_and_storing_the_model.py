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
iters = 10

with open(f"json_files/gesturespersons1-14WOhitting.json", 'r') as file:
    data = json.load(file)
#the frames
X_data = np.array([d["frame"] for d in data])
#the labels
#dictkey = {'t': "petting", 'k': "poking", 'c': "comforting", 'h': "hitting", 's': "scratching"}
dictkey = {'regular': 0, 'petting': 1, 'poking': 2, 'comforting': 3, 'scratching': 4}
y_data = np.array([dictkey[d["label"]] for d in data])
print(y_data)

X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.25)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2)

batch_size = 16


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
X_val, y_val = drop_remain(X_val, y_val)

#newmodel734_704_1-14
#Mo_B16_741_700_1-14
#Mo_B16_712_706_1-14.h5
#MO_B16_781_761_1-14WOH
model = models.Sequential()
model.add(layers.LSTM(128, stateful=True, return_sequences=True))
model.add(layers.LSTM(128, stateful=True, return_sequences=True))
model.add(layers.LSTM(128, stateful=True))
model.add(layers.Dense(5))

'''model = models.Sequential()
model.add(layers.LSTM(64, stateful=True, return_sequences=True))
model.add(layers.LSTM(64, stateful=True, return_sequences=True))
model.add(layers.LSTM(64, stateful=True))
model.add(layers.Dense(6))'''

'''model = models.Sequential()
model.add(layers.LSTM(32, stateful=True, return_sequences=True))
model.add(layers.LSTM(32, stateful=True, return_sequences=True))
model.add(layers.LSTM(32, stateful=True, return_sequences=True))
model.add(layers.Dense(6))'''



model.compile(optimizer='adam',
              loss=losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
#hist = {'loss':[],'accuracy':[]}
hist = {'loss':[],'accuracy':[],'val_loss':[],'val_accuracy':[]}
for i in range(iters):
    #epoch_hist = model.fit(X_train,y_train, epochs=1, batch_size=batch_size, verbose=2, shuffle=False)
    epoch_hist = model.fit(X_train, y_train, validation_data=(X_val, y_val),
                           epochs=1, batch_size=batch_size, verbose=2, shuffle=False)
    for key in hist.keys():
        hist[key].append(epoch_hist.history[key])

    for layer in model.layers:
        if layer.name == 'lstm':
            layer.reset_states()


#graph to show the accuracy of the model
plt.plot(hist['accuracy'], label='accuracy')
#
plt.plot(hist['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()

#save the model
model.save('MO_without_hitting.h5')

test_loss, test_acc = model.evaluate(X_test,  y_test, verbose=2, batch_size=batch_size)
print(test_loss, test_acc)

y_pred = model.predict(X_test, batch_size=batch_size)
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



