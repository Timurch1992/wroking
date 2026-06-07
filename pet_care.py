# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: PetCare
import datetime

def init_pet_care():
    pets = {
        "Рекс": {"вид": "Собака", "возраст": 3, "вес": 25.0, "привит": True},
        "Мурзик": {"вид": "Кошка", "возраст": 1, "вес": 4.5, "привит": False}
    }
    
    logs = {
        "Рекс": [],
        "Мурзик": []
    }
    
    notes = {
        "Рекс": "Любит мяч и длинные прогулки.",
        "Мурзик": "Не любит, когда берут на руки."
    }
    
    last_feed = datetime.datetime.now()
    
    return pets, logs, notes, last_feed

pets, logs, notes, last_feed = init_pet_care()
