# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: PetCare
def print_pet_table(pet_name, feeds, walks, health, notes):
    """Выводит таблицу ухода за питомцем в консоль."""
    border = "+" + "-" * 20 + "+" + "-" * 15 + "+" + "-" * 15 + "+" + "-" * 20 + "+"
    header = (
        "PetName" + "|" +
        f"{len(feeds):>3}" + "Feeds|" +
        f"{len(walks):>3}" + "Walks|" +
        f"{len(health):>3}" + "Health|" +
        f"{len(notes):>3}" + "Notes|"
    )
    print(border)
    print(header)
    print(border)

    for name, feed_log in zip(pet_name, feeds):
        health_count = len(health) if isinstance(health, list) else 0
        walk_count = len(walks) if isinstance(walks, list) else 0
        note_count = len(notes) if isinstance(notes, list) else 0

        feed_str = str(feed_log)[:15] if feed_log else "-"
        walk_str = f"{walk_count}" if not isinstance(walks, list) else (str(walks[0])[:14] if walks else "-")
        health_str = "OK" if health_count == 0 else f"{health_count}"
        note_str = str(notes[0])[:18] if notes and isinstance(notes, list) else "-"

        print(f"|{name:^20}|{feed_str:>3}|{walk_str:>15}|{health_str:>15}|{note_str} |")
    print(border)
