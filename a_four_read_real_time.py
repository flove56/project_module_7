#! /usr/bin/python3
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

class real_time_reading:
    dim_row = 27
    dim_col = 19

    # batch_size = 8
    batch_size = 16

    type = {0: 'reg', 1: 'pet', 2: 'pok', 3: 'com', 4: 'scr'}
    labels = []

    model = load_model('MO_B16_781_761_1-14WOH.h5')

    TSP = TSPDecoder(port="COM10", rows=dim_row, columns=dim_col)  # Femke's working line
    #TSP = TSPDecoder(rows=dim_row, columns=dim_col)  # Maja's working line


    def do_one_reading(self):

        if self.TSP.available():
            frames = np.array([self.TSP.readFrame() for i in range(self.batch_size)])

            #thresholding
            frames[frames < 30] = 0

            predictions = self.model.predict(frames)
            predicted_labels = np.argmax(predictions, axis = 1)

            self.labels.append(self.type[predicted_labels[1]])


    def get_the_smooth_state(self, previous_state):
        if len(self.labels) <= 20:
            return previous_state
        else:
            amount_type = {'reg': 0, 'pet': 0, 'pok': 0, 'com': 0, 'scr': 0}
            for d in self.labels:
                for key in amount_type:
                    if d == key:
                        amount_type[key] += 1
            maximum = max(zip(amount_type.values(), amount_type.keys()))[1]
            self.labels = []
            return maximum