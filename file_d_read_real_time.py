from TSPDecoder import *
import numpy as np
from keras.models import load_model

class real_time_reading:
    # Initialize the number of rows and columns, and the batch size
    dim_row = 27
    dim_col = 19
    batch_size = 16

    # Create a dictionary for the labels
    type = {0: 'reg', 1: 'pet', 2: 'pok', 3: 'com', 4: 'scr'}
    # Make an empty list to store the read labels in
    labels = []

    # Load the model to use for classification
    model = load_model('MO_B16_916_902_1-20WOHpokerpetter.h5')

    # Initialize the TSPDecoder
    TSP = TSPDecoder(port="COM10", rows=dim_row, columns=dim_col)  # Femke's working line
    #TSP = TSPDecoder(rows=dim_row, columns=dim_col)  # Maja's working line


    # Get the data from one set of frames and store the label in the list labels
    def do_one_reading(self):

        if self.TSP.available():
            # Read a batch of frames with the TSP
            frames = np.array([self.TSP.readFrame() for i in range(self.batch_size)])

            # Remove the noise by adding a threshold
            frames[frames < 30] = 0

            # Predict the label
            predictions = self.model.predict(frames)
            predicted_labels = np.argmax(predictions, axis = 1)

            # Add the label to the list of labels
            self.labels.append(self.type[predicted_labels[1]])


    def get_the_smooth_state(self, previous_state):
        # If there are less than 20 collected labels, continue getting labels
        if len(self.labels) < 20:
            return previous_state
        # If ther are 20 labels, count how often the labels occur and return the label that occurs the most.
        else:
            amount_type = {'reg': 0, 'pet': 0, 'pok': 0, 'com': 0, 'scr': 0}
            # Count the labels
            for d in self.labels:
                amount_type[d] += 1

            # Find which type occurs most
            maximum = max(zip(amount_type.values(), amount_type.keys()))[1]
            # Empty the labels list
            self.labels = []
            return maximum