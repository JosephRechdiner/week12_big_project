import os
import json

PATH = "./data/"

def read_json():
    all_json_list = []
    for filename in os.listdir(PATH):
        # every file in this dir has a different path
        full_path = f"{PATH}{filename}"
        with open(full_path, "r") as file:
            json_data = json.load(file)
            all_json_list.append(json_data)

    # making the data one big list[dict] (every json file is a list[dict])
    simplefied_json = simplefy_multiple_json(all_json_list)
    return simplefied_json

def simplefy_multiple_json(json_files: list[list]):
    result = []
    for json_file in json_files:
        for event in  json_file:
            result.append(event)
    return result   