# record.py
import json

def load_record():
    try:
        with open("record.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_record(record):
    with open("record.json", "w") as f:
        json.dump(record, f)

def add_to_record(food, calories):
    record = load_record()
    if food in record:
        record[food] += calories
    else:
        record[food] = calories
    save_record(record)

def get_record():
    return load_record()
