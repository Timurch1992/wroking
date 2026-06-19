# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: PetCare
import json, os, datetime

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        pets = data.get("pets", [])
        logs = data.get("logs", [])
        notes = data.get("notes", [])
        
        if not pets and not logs and not notes:
            return {"status": "empty"}, None, None
        
        now = datetime.datetime.now()
        for pet in pets:
            pet["id"] = len(pets) + 1
            pet["created_at"] = str(now.date())
        
        if logs:
            for log in logs:
                log["timestamp"] = log.get("timestamp", str(now))
            
            def get_last_log_by_pet(logs, pet_id):
                return next((l for l in logs if l.get("pet_id") == pet_id), None)

        if notes:
            for note in notes:
                note["created_at"] = note.get("created_at", str(now.date()))
        
        return {"status": "loaded"}, pets, logs, notes
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {"status": "error", "message": str(e)}, None, None, None

INITIAL_JSON = '''
{
  "pets": [
    {"name": "Рекс", "type": "собака", "age": 3},
    {"name": "Мурка", "type": "кошка", "age": 1}
  ],
  "logs": [
    {"pet_id": 1, "activity": "кормление", "value": 250, "timestamp": "2023-10-27T08:00"},
    {"pet_id": 2, "activity": "прогулка", "duration_minutes": 45}
  ],
  "notes": [
    {"text": "Рекс любит мяч.", "created_at": "2023-10-26"}
  ]
}
'''

if __name__ == "__main__":
    result, pets_data, logs_data, notes_data = load_initial_data(INITIAL_JSON)
    if result["status"] == "loaded":
        print(f"Загружено {len(pets_data)} питомцев")
