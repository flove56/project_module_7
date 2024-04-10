import json
import numpy as np

all_data = []
with open(f"json_files/gesturesperson10.json", 'r') as file:
    data = json.load(file)
    for d in data:
        all_data.append(d)

with open(f"json_files/gesturesregular.json.json", 'r') as file:
    data = json.load(file)
    for d in data:
        all_data.append(d)

with open('json_files/gesturesperson10WITHr.json', 'w') as json_file:
    json.dump(all_data, json_file, indent=4)
