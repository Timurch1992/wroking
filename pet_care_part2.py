# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: PetCare
class PetData:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    @property
    def is_adult(self):
        return self.age >= 1

    def validate_input(self, raw_name, raw_age, raw_breed):
        try:
            name = raw_name.strip().title()
            if not name or len(name) > 50:
                raise ValueError("Имя должно быть от 1 до 50 символов.")
            age = int(raw_age)
            if age < 0 or age > 30:
                raise ValueError("Возраст должен быть от 0 до 30 лет.")
            breed = raw_breed.strip().title()
            if not breed or len(breed) > 100:
                raise ValueError("Порода должна быть от 1 до 100 символов.")
            return PetData(name, age, breed)
        except ValueError as e:
            print(f"Ошибка валидации: {e}")
            return None

    def add_feeding(self, amount_grams):
        if not isinstance(amount_grams, (int, float)) or amount_grams <= 0:
            raise ValueError("Количество корма должно быть положительным числом.")
        self.last_feeding = {'amount': amount_grams, 'timestamp': 'now'}

    def add_health_note(self, symptom):
        if not symptom or len(symptom) > 200:
            raise ValueError("Симптом должен быть от 1 до 200 символов.")
        self.health_notes.append({'symptom': symptom, 'timestamp': 'now'})

    def add_walk(self, duration_minutes):
        if not isinstance(duration_minutes, (int, float)) or duration_minutes <= 0:
            raise ValueError("Длительность прогулки должна быть положительным числом.")
        self.last_walk = {'duration': duration_minutes, 'timestamp': 'now'}

    def add_note(self, text):
        if not text or len(text) > 500:
            raise ValueError("Заметка должна быть от 1 до 500 символов.")
        self.notes.append({'text': text, 'timestamp': 'now'})
