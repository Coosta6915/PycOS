import json


def load(file_path: str):
    with open(file_path, "rt") as f_json_load:
        json_data = json.load(f_json_load)
        return json_data


def dump(file_path: str, json_data):
    with open(file_path, "wt") as f_json_dump:
        json.dump(json_data, f_json_dump, indent=4)
