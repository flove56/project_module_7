import serial
import cv2
import numpy as np
import time
import json

from TSPDecoder import *

# Compare the input key with numbers
#keys = ['t', 'k', 'c', 'h', 's']
dictkey = {'r': "regular", 't': "petting", 'k': "poking", 'c': "comforting", 'h': "hitting", 's': "scratching"}

rows, columns = 27, 19
TSP = TSPDecoder(port = "COM10", rows=rows, columns=columns)
all_data = []
separation = True

# Initialize last_img for the first comparison with thresed_img
last_img = TSP.readFrame()

while True:
    data = {
        "time": int,
        "label": '',
        "sep": separation,
        "frame": []
    }

    img = TSP.readFrame()
    #################################################################################np.maximum???
    # Add a threshold to the pixels
    ret, thresed_img = cv2.threshold(img, 30, 255, cv2.THRESH_TOZERO)
    # Add the previous frame over the thresed_img
    #thresed_img = cv2.add(thresed_img, last_img)

    # Remove noise that last_img might have added
    #ret, img_tr= cv2.threshold(thresed_img, 50, 255, cv2.THRESH_TOZERO)
    # Set the values that are higher than 255 because of the addition to 255
    #ret, img_to_save = cv2.threshold(img_tr, 255, 255, cv2.THRESH_TRUNC)
    # put the image into data["frame"]
    #data["frame"] = img_to_save.tolist()
    data["frame"] = thresed_img.tolist()


    # Resize the data["frame"] to make it bigger so the window will be easier to see.
    window_img = cv2.resize(thresed_img, (270, 190))
    cv2.imshow('beeld', window_img)

    # Save the last image
    #last_img = thresed_img

    # Read the key input
    key = AsciiDecoder(cv2.waitKey())

    # Stop the program when q is pressed
    if key == 'q':
        # the json file is opened and the data is put into the file
        with open('json_files/gesturesperson16.json', 'w') as json_file:
            json.dump(all_data, json_file, indent=4)
        quit()

    if key in dictkey:
        data["label"] = dictkey[key]
        # the timestamp is saved into data["time"]
        data["time"] = time.time()
        all_data.append(data)
        # After the data is stored separation is set to False, because the number is still being drawn
        separation = False

    # Clear the screen when c is pressed and get ready for the next number
    if key == 'n':
        # The separation is set to True because the next image will be the first image of the next number
        separation = True
        # The screen is cleared by reading the now empty frame
        last_img = TSP.readFrame()
