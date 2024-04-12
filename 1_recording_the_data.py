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

while True:
    data = {
        "time": int,
        "label": '',
        "sep": separation,
        "frame": []
    }

    img = TSP.readFrame()
    ret, thresed_img = cv2.threshold(img, 30, 255, cv2.THRESH_TOZERO)


    data["frame"] = thresed_img.tolist()


    window_img = cv2.resize(thresed_img, (270, 190))
    cv2.imshow('beeld', window_img)

    # Read the key input
    key = AsciiDecoder(cv2.waitKey())
    print(key)
    # Stop the program when q is pressed
    if key == 'q':
        # the json file is opened and the data is put into the file
        with open('json_files/deletethis.json', 'w') as json_file:
            json.dump(all_data, json_file, indent=4)
        quit()

    if key in dictkey:
        data["label"] = dictkey[key]
        # the timestamp is saved into data["time"]
        data["time"] = time.time()
        all_data.append(data)
        # After the data is stored separation is set to False
        separation = False

    # Start a new gesture
    if key == 'n':
        # The separation is set to True because the next image will be the first image of the next gesture
        separation = True
