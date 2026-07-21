# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: PetCare
def show_metrics(pets_data, logs):
    total_entries = len(logs)
    feed_count = sum(1 for l in logs if "кормление" in l.get("тип", "").lower())
    health_count = sum(1 for l in logs if "здоровье" in l.get("тип", "").lower())
    walk_count = sum(1 for l in logs if "прогулка" in l.get("тип", "").lower())
    note_count = sum(1 for l in logs if "заметка" in l.get("тип", "").lower())

    print(f"\n📊 Метрики проекта PetCare:")
    print(f"  Всего записей:       {total_entries}")
    print(f"  Записи о кормлении:   {feed_count}")
    print(f"  Записи о здоровье:    {health_count}")
    print(f"  Записи о прогулках:   {walk_count}")
    print(f"  Заметки:              {note_count}")

    if pets_data:
        for name, data in pets_data.items():
            age = data.get("возраст", "неизвестен")
            breed = data.get("порода", "неизвестна")
            print(f"\n🐾 Питомец: {name}")
            print(f"  Возраст:    {age} лет")
            print(f"  Порода:     {breed}")

if __name__ == "__main__":
    pets_data = {"Рекс": {"возраст": 3, "порода": "лабрадор"}, "Белка": {"возраст": 1.5, "порода": "альбинос"}}
    logs = [
        {"тип": "кормление", "питомец": "Рекс", "дата": "2024-06-01"},
        {"тип": "здоровье", "питомец": "Белка", "дата": "2024-06-02"},
        {"тип": "прогулка", "питомец": "Рекс", "дата": "2024-06-03"},
        {"тип": "заметка", "питомец": "Белка", "дата": "2024-06-04"},
    ]
    show_metrics(pets_data, logs)
