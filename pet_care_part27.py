# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: PetCare
def reset_demo_data():
    """Сбрасывает все данные в дефолтные значения."""
    pets = [
        {"id": 1, "name": "Рекс", "species": "собака", "age_months": 24, "weight_kg": 30},
        {"id": 2, "name": "Мурка", "species": "кошка", "age_months": 18, "weight_kg": 5},
    ]
    records = {
        "feedings": [
            {"pet_id": 1, "amount_g": 200, "timestamp": None},
            {"pet_id": 2, "amount_g": 60, "timestamp": None},
        ],
        "walks": [],
        "health_logs": [],
        "notes": [],
    }
    global pets_data, records_data, current_pet, last_action
    pets_data = pets
    records_data = records
    current_pet = 1
    last_action = None


def clear_state():
    """Очищает все данные и возвращает в начальное состояние."""
    reset_demo_data()
