import json
import numpy as np

# Open the file that contains hitting
with open(f"json_files/gesturespersons1-20WOhitting..json", 'r') as file:
    data = json.load(file)

empty = np.zeros(shape=(27, 19))

# Add everything with a different label than poking to the filtered data list and
# if the label is poking and it is the first frame, add it to the filtered data and
# of the rest of the poking data only add the frames that are not empty
filtered_data = [entry for entry in data if entry['label'] != 'poking' or
                 (entry['label'] == 'poking' and entry['sep'] == True) or
                 (entry['label'] == 'poking' and np.any(entry['frame'] != empty))]

# Save the filtered data in a new json file
with open('json_files/gesturespersons1-20WOhitting_pokeEmptiesRemoved..json', 'w') as json_file:
    json.dump(filtered_data, json_file, indent=4)
