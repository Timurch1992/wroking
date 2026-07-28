# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: PetCare
class PetCareApp:
        def __init__(self):
            self._actions = []

        def _record(self, action_type, **kwargs):
            self._actions.append({"type": action_type, "data": kwargs})

        def undo_last(self):
            if not self._actions: return None
            last = self._actions.pop()
            if last["type"] == "feed":
                self._record("unfeed", amount=last["data"]["amount"], pet_name=last["data"]["pet_name"])
            elif last["type"] == "walk":
                duration = last["data"].get("duration", 0)
                self._record("unwalk", duration=duration, pet_name=last["data"]["pet_name"])
            elif last["type"] == "health_check":
                result = last["data"]["result"]
                if result == "good": self._record("mark_health_bad", pet_name=last["data"]["pet_name"])
                else: self._record("mark_health_good", pet_name=last["data"]["pet_name"])
            elif last["type"] == "note":
                self._record("delete_note", content=last["data"]["content"], pet_name=last["data"]["pet_name"])
            return last

        def feed(self, pet_name, amount):
            self._record("feed", pet_name=pet_name, amount=amount)
            print(f"[{pet_name}] Корм: {amount}г")

        def walk(self, pet_name, duration=30):
            self._record("walk", pet_name=pet_name, duration=duration)
            print(f"[{pet_name}] Прогулка: {duration} мин")

        def check_health(self, pet_name):
            result = "good" if hash(pet_name) % 2 else "needs_attention"
            self._record("health_check", pet_name=pet_name, result=result)
            print(f"[{pet_name}] Здоровье: {result}")

        def add_note(self, pet_name, content):
            self._record("note", pet_name=pet_name, content=content)
            print(f"[{pet_name}] Заметка: {content[:30]}...")
