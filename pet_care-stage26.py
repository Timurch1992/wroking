# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: PetCare
def demo_commands():
    """Демо-команды для быстрого ручного тестирования."""
    while True:
        cmd = input("\n>>> Demo command (q to quit): ").strip().lower()
        if cmd == 'q':
            break
        elif cmd in ('feed', 'walk'):
            print(f"  -> Pet {cmd}ed successfully.")
        elif cmd == 'health':
            print("  -> Health check passed. Heart rate: 120 bpm, Temp: 38.5°C")
        elif cmd == 'note':
            note = input("    Enter a note: ").strip() or "No note provided"
            print(f"  -> Note saved: {note}")
        else:
            print(f"  -> Unknown command: {cmd}. Type 'feed', 'walk', 'health', 'note' for demo.")


demo_commands()
