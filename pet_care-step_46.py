# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: PetCare
def migrate():
    """Миграция структуры данных: добавляем колонку 'activity_log' в таблицу pets."""
    if 'activity_log' not in pets:
        pets['activity_log'] = []
    return pets
