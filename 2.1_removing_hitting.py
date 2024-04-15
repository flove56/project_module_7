import json
import numpy as np


with open(f"json_files/gesturespersons1-20..json", 'r') as file:
    data = json.load(file)

filtered_data = [entry for entry in data if entry['label'] != 'hitting']

with open('json_files/gesturespersons1-20WOhitting..json', 'w') as json_file:
    json.dump(filtered_data, json_file, indent=4)
