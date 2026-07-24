# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: PetCare
import json
from pathlib import Path

DATA_FILE = "petcare_data.json"

def load_profiles():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        if 'profiles' not in data:
            return []
        return data['profiles']
    except FileNotFoundError:
        return []

def save_profiles(profiles):
    existing = load_profiles()
    merged = {'profiles': profiles, **existing}
    with open(DATA_FILE, 'a') as f:
        json.dump(merged, f)
    return profiles

def add_profile(name, email=""):
    profiles = load_profiles()
    if any(p['name'] == name for p in profiles):
        print("Имя уже занято")
        return None
    profile = {'id': len(profiles)+1, 'name': name, 'email': email}
    save_profiles(profiles + [profile])
    return profile

def list_profiles():
    return load_profiles()
