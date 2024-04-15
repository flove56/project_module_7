import json
import numpy as np

# Open the file that contains hitting
with open(f"json_files/gesturespersons1-20..json", 'r') as file:
    data = json.load(file)

# Add everything with a different label than hitting to the filtered data list
filtered_data = [entry for entry in data if entry['label'] != 'hitting']

# Save the filtered data in a new json file
with open('json_files/gesturespersons1-20WOhitting..json', 'w') as json_file:
    json.dump(filtered_data, json_file, indent=4)
