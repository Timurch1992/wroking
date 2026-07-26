# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: PetCare
def switch_profile():
    """Переключить активный профиль пользователя."""
    global active_user_id, current_profile
    if not profiles:
        print("Нет доступных профилей.")
        return
    print("\n=== Доступные профили ===")
    for i, p in enumerate(profiles):
        marker = " (активен)" if p["user_id"] == active_user_id else ""
        print(f"  {i+1}. {p['name']} — возраст: {p.get('age', '—')}, статус: {marker}")
    choice = input("Выберите номер профиля (или Enter для выхода): ").strip()
    if not choice or int(choice) < 1 or int(choice) > len(profiles):
        print("Профиль не выбран. Операция отменена.")
        return
    idx = int(choice) - 1
    new_profile = profiles[idx]
    active_user_id = new_profile["user_id"]
    current_profile = copy.deepcopy(new_profile)
    # Обновляем текущие данные питомца под нового владельца, если есть привязка
    if "pet_owner" in current_pet and current_pet["pet_owner"] == active_user_id:
        print(f"\nПрофиль переключён на {current_profile['name']}. Данные питомца обновлены.")
    else:
        print(f"\nПрофиль переключён на {current_profile['name']}.")
