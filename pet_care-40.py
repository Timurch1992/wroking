# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: PetCare
import argparse

def main():
    parser = argparse.ArgumentParser(description="PetCare - Трекер ухода за питомцем")
    subparsers = parser.add_subparsers(dest="command")

    feed_parser = subparsers.add_parser("feed", help="Записать кормление")
    feed_parser.add_argument("--name", required=True, help="Имя питомца")
    feed_parser.add_argument("--food", required=True, help="Тип корма")
    feed_parser.add_argument("--amount", type=float, required=True, help="Количество (г)")

    health_parser = subparsers.add_parser("health", help="Записать состояние здоровья")
    health_parser.add_argument("--name", required=True, help="Имя питомца")
    health_parser.add_argument("--temp", type=float, help="Температура (°C)")
    health_parser.add_argument("--notes", help="Заметки о здоровье")

    walk_parser = subparsers.add_parser("walk", help="Записать прогулку")
    walk_parser.add_argument("--name", required=True, help="Имя питомца")
    walk_parser.add_argument("--duration", type=float, help="Продолжительность (мин)")
    walk_parser.add_argument("--distance", type=float, help="Расстояние (км)")

    note_parser = subparsers.add_parser("note", help="Добавить заметку")
    note_parser.add_argument("--name", required=True, help="Имя питомца")
    note_parser.add_argument("--text", required=True, help="Текст заметки")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return
    print(f"PetCare: {args.command} - команда принята")
    if args.command == "feed":
        print(f"  Питомец: {args.name}, корм: {args.food}, кол-во: {args.amount}г")
    elif args.command == "health":
        print(f"  Питомец: {args.name}, темп: {args.temp}, заметки: {args.notes}")
    elif args.command == "walk":
        print(f"  Питомец: {args.name}, длительность: {args.duration} мин, расстояние: {args.distance} км")
    elif args.command == "note":
        print(f"  Питомец: {args.name}, заметка: {args.text}")

if __name__ == "__main__":
    main()
