# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: PetCare
import time

class PetCare:
    def __init__(self):
        self.records = []
        self.last_timestamp = int(time.time())

    def add_feeding(self, pet_name, food_type, amount_grams):
        record = {
            "type": "feeding",
            "timestamp": self.last_timestamp,
            "pet": pet_name,
            "details": {"food": food_type, "amount": amount_grams}
        }
        self.records.append(record)
        return record

    def add_health_check(self, pet_name, symptom, status):
        record = {
            "type": "health",
            "timestamp": self.last_timestamp,
            "pet": pet_name,
            "details": {"symptom": symptom, "status": status}
        }
        self.records.append(record)
        return record

    def add_walk(self, pet_name, duration_minutes, weather):
        record = {
            "type": "walk",
            "timestamp": self.last_timestamp,
            "pet": pet_name,
            "details": {"duration": duration_minutes, "weather": weather}
        }
        self.records.append(record)
        return record

    def add_note(self, pet_name, note_text):
        record = {
            "type": "note",
            "timestamp": self.last_timestamp,
            "pet": pet_name,
            "details": {"text": note_text}
        }
        self.records.append(record)
        return record

    def get_recent_records(self, limit=5):
        return self.records[-limit:] if len(self.records) >= limit else self.records[:]
