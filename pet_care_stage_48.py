# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: PetCare
def _normalize_pet_name(name: str) -> str:
    """Убирает пробелы, приводит к нижнему регистру и экранирует спецсимволы."""
    return re.sub(r"[^a-zA-Z0-9а-яА-ЯёЁ_]", "_", name.strip().lower())

def _format_pet_name(name: str) -> str:
    """Восстанавливает читаемый вид: заменяет _ на пробел и заглавливает."""
    return re.sub(r"_", " ", name.strip().title())
