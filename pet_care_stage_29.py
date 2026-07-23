# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: PetCare
def load_config():
    config = {
        "app_name": "PetCare",
        "version": 29,
        "pet_types": ["dog", "cat", "hamster"],
        "feeding_times": [600, 1800],
        "health_check_interval": 3600,
        "walk_duration_min": 30,
        "max_notes_per_day": 5,
    }
    return config

def get_config():
    global _app_config
    if _app_config is None:
        _app_config = load_config()
    return _app_config

_app_config = None
