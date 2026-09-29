# Functions used to save and load project data

import json


def load_data():
    try:
        with open("data/expenses.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(expenses):
    with open("data/expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
