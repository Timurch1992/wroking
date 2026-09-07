# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: PetCare
def demo():
    pet = Pet("Рекс", "Собака")
    pet.set_age(3)
    pet.set_weight(12.5)
    pet.set_mood("Счастливый")
    pet.set_health("Отлично")

    pet.feed("Корм для собак", 200, "Вкусный")
    pet.walk("Парк у реки", 30)
    pet.sleep()
    pet.play("Полная свобода")

    pet.set_health("Неплохо")
    pet.vet_checkup("Вакцинация", "Без проблем")

    pet.add_note("Рекс любит играть с мячом")
    pet.add_note("Не забыть купить новый ошейник")

    print(f"Имя: {pet.name}")
    print(f"Возраст: {pet.age} лет")
    print(f"Вес: {pet.weight} кг")
    print(f"Мood: {pet.mood}")
    print(f"Здоровье: {pet.health}")
    print(f"Последняя прогулка: {pet.last_walk}")
    print(f"Последний сон: {pet.last_sleep}")
    print(f"Последняя игра: {pet.last_play}")
    print(f"Заметки: {pet.notes}")
    print(f"Последний осмотр: {pet.last_vet}")
    print("Демо PetCare завершено!")
