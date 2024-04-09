import json
import numpy as np

all_data = []
with open(f"json_files/gesturesperson1.json", 'r') as file:
    data = json.load(file)
    for d in data:
        all_data.append(d)

with open(f"json_files/gesturesperson2.json", 'r') as file:
    data = json.load(file)
    for d in data:
        all_data.append(d)

with open('json_files/gesturespersons.json', 'w') as json_file:
    json.dump(all_data, json_file, indent=4)
