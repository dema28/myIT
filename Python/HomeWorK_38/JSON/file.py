import json
import os

FILE_PATH = "users.json"

def save_users(users):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

def load_users():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []
