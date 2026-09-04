# === Stage 45: Добавь восстановление из резервной копии ===
# Project: PetCare
import json
import os

def load_backup(filename="backup.json"):
    if not os.path.exists(filename):
        print(f"Резервная копия '{filename}' не найдена.")
        return None
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Резервная копия успешно загружена из '{filename}'.")
    return data

def save_current_as_backup(filename="backup.json"):
    with open("petcare_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Текущие данные сохранены в '{filename}'.")
