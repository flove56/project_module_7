import serial
import cv2
import numpy as np
import time
import json
from TSPDecoder import *

# Make a dictionary to link the pressed key to an action
dict_key = {'r': "regular", 't': "petting", 'k': "poking", 'c': "comforting", 'h': "hitting", 's': "scratching"}

# Initialize the TSPDecoder
rows, columns = 27, 19
TSP = TSPDecoder(port = "COM10", rows=rows, columns=columns)

# Make an empty list to store the data
all_data = []
# Start with separation as true for the first gesture
separation = True

# Continuously loop to gather data with the keys and save the data when pressing q
while True:
    # Make a dictionary with the time, label, seperation, and the frame
    data = {
        "time": int,
        "label": '',
        "sep": separation,
        "frame": []
    }

    # Read the frame and add a threshold to remove noise
    img = TSP.readFrame()
    ret, thresed_img = cv2.threshold(img, 30, 255, cv2.THRESH_TOZERO)

    # Add the image to the data dictionary in the "frame" category
    data["frame"] = thresed_img.tolist()

    # Show the frame in a window to monitor the data-collecting during the collecting process
    window_img = cv2.resize(thresed_img, (270, 190))
    cv2.imshow('beeld', window_img)

    # Read the key input
    key = AsciiDecoder(cv2.waitKey())

    # Stop the program when q is pressed
    if key == 'q':
        # The json file is opened and the data is put into the file
        with open('json_files/gesturesperson21.json', 'w') as json_file:
            json.dump(all_data, json_file, indent=4)
        quit()

    # Put the right label on the frame and give it a timestamp. Then add it to the list of all_data
    if key in dict_key:
        data["label"] = dict_key[key]
        # The timestamp is saved into data["time"]
        data["time"] = time.time()

        all_data.append(data)
        # After the data is stored separation is set to False
        separation = False

    # Start a new gesture
    if key == 'n':
        # The separation is set to True because the next image will be the first image of the next gesture
        separation = True
