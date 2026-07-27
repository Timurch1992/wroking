# === Stage 32: Добавь журнал действий пользователя ===
# Project: PetCare
import json
from datetime import datetime, date

def load_log(log_path='petcare_log.json'):
    try:
        with open(log_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_log(log, log_path='petcare_log.json'):
    with open(log_path, 'w') as f:
        json.dump(log, f, indent=2, ensure_ascii=False)

def add_action(action_type, pet_name=None, details='', user_name='PetCare'):
    """Добавить запись в журнал действий."""
    log = load_log()
    entry = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'user': user_name,
        'type': action_type,
        'target': pet_name or 'system',
        'details': details
    }
    log.append(entry)
    save_log(log)
    return entry

def get_history(action_type=None, limit=50):
    """Получить историю действий с опциональным фильтром и лимитом."""
    log = load_log()
    if action_type:
        log = [e for e in log if e['type'] == action_type]
    return log[-limit:]

def print_history(action_type=None, limit=50):
    """Вывести историю действий в консоль."""
    history = get_history(action_type, limit)
    if not history:
        print("\nЖурнал пуст.")
        return
    print(f"\n{'='*40}")
    print(f"  Журнал действий ({len(history)} записей)")
    print(f"{'='*40}")
    for i, entry in enumerate(history, 1):
        print(f"{i}. [{entry['timestamp']}] {entry['target']} — {entry['details']}")

def reset_log():
    """Очистить журнал действий."""
    save_log([])
    return True
