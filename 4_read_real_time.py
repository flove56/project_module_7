#! /usr/bin/python3
import json
import os
from TSPDecoder import *
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras import models, layers, losses
import cv2
from keras.models import load_model


#with open(f"{os.path.dirname(os.path.realpath(__file__))}/Data/Sets/all_frames.json", 'r') as file:
#    jsondata = json.load(file)

#X = np.array([line["frame"] for line in jsondata])
#y = np.array([int(line["label"]) for line in jsondata])

dim_row = 27
dim_col = 19
#iters = 5

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
#X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

batch_size = 8


#def drop_remain(X, y):
#    remain = X.__len__() % batch_size
#    if remain == 0:
#        return X, y
#    else:
#        X = X[:-remain, :, :]
#        y = y[:-remain]
#        return X, y


#X_train, y_train = drop_remain(X_train, y_train)
#X_test, y_test = drop_remain(X_test, y_test)
#X_val, y_val = drop_remain(X_val, y_val)

#odel = models.Sequential()
#model.add(layers.LSTM(128, stateful=True, return_sequences=True))
#model.add(layers.LSTM(128, stateful=True, return_sequences=True))
#model.add(layers.LSTM(128, stateful=True))
#model.add(layers.Dense(10))

#model.compile(optimizer='adam',
#              loss=losses.SparseCategoricalCrossentropy(from_logits=True),
#              metrics=['accuracy'])
#hist = {'loss': [], 'accuracy': [], 'val_loss': [], 'val_accuracy': []}
#for i in range(iters):
#    epoch_hist = model.fit(X_train, y_train, validation_data=(X_val, y_val),
#                           epochs=1, batch_size=batch_size, verbose=2, shuffle=False)
#    for key in hist.keys():
#        hist[key].append(epoch_hist.history[key])

#    for layer in model.layers:
#        if layer.name == 'lstm':
#            layer.reset_states()

# plt.plot(hist['accuracy'], label='accuracy')
# plt.plot(hist['val_accuracy'], label='val_accuracy')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.ylim([0.5, 1])
# plt.legend(loc='lower right')
# plt.show()


#test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2, batch_size=batch_size)
#print(f"Test loss: {test_loss}, Test acc: {test_acc}")

# print(f"Prediction: {model.predict(np.expand_dims(X_test[0], axis=0))[0].argmax()}")

model = load_model('model719_711MF6.h5')

TSP = TSPDecoder(port= "COM10",rows=dim_row, columns=dim_col)
while TSP.available():
    frames = np.array([TSP.readFrame() for i in range(batch_size)])

    #thresholding
    frames[frames < 50] = 0

    predictions = model.predict(frames)
    predicted_labels = np.argmax(predictions, axis = 1)
    for label in predicted_labels:
        print(label)

    #key_from_wait_key = cv2.waitKey(1)
    #key = AsciiDecoder(key_from_wait_key)
    key = AsciiDecoder(cv2.waitKey())

    if key == 'q':
        exit()