# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: PetCare
import json, os

DATA_FILE = "petcare_data.json"

def save_to_json(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return {"pets": [], "logs": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"pets": [], "logs": []}

def init_storage():
    data = load_from_json()
    save_to_json(data)
