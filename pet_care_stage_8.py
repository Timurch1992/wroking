# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: PetCare
def show_menu():
    print("\n=== Меню PetCare ===")
    print("1. Добавить кормление")
    print("2. Записать прогулку")
    print("3. Отметить здоровье")
    print("4. Создать заметку")
    print("5. Просмотреть историю")
    print("0. Выход")
    try:
        choice = input("Выберите действие (0-5): ")
        return int(choice)
    except ValueError:
        print("Неверный ввод.")
        return None

def handle_feeding():
    name = input("Имя питомца: ").strip() or "Мой питомец"
    amount = float(input("Количество корма (г): "))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[{timestamp}] {name} съел {amount} г.")

def handle_walk():
    name = input("Имя питомца: ").strip() or "Мой питомец"
    duration = float(input("Длительность (мин): "))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[{timestamp}] {name} погулял {duration} мин.")

def handle_health():
    name = input("Имя питомца: ").strip() or "Мой питомец"
    status = input("Состояние (хорошо/плохо): ").strip().lower()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[{timestamp}] {name}: статус '{status}'.")

def handle_note():
    name = input("Имя питомца: ").strip() or "Мой питомец"
    text = input("Заметка: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[{timestamp}] {name}: '{text}'.")

def handle_history():
    name = input("Имя питомца (оставьте пустым для всех): ").strip() or ""
    if not history_data:
        print("История пуста.")
        return
    for entry in history_data.get(name, []):
        print(f"{entry['time']} - {entry['type']}: {entry['value']}")

if __name__ == "__main__":
    while True:
        choice = show_menu()
        if choice is None:
            continue
        elif choice == 1:
            handle_feeding()
        elif choice == 2:
            handle_walk()
        elif choice == 3:
            handle_health()
        elif choice == 4:
            handle_note()
        elif choice == 5:
            handle_history()
        elif choice == 0:
            print("Выход из программы.")
            break
