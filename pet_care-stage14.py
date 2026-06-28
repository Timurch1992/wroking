# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: PetCare
def generate_summary(pets, logs):
    now = datetime.now()
    today_start = replace(now, hour=0, minute=0, second=0, microsecond=0)
    summary_lines = ["=== PetCare Сводка ===", f"Время: {now.strftime('%Y-%m-%d %H:%M')}", ""]

    for pet in pets.values():
        pet_logs = [l for l in logs if l['pet_id'] == pet['id']]
        today_logs = [l for l in pet_logs if replace(l['timestamp'], tzinfo=timezone.utc).replace(tzinfo=None) >= today_start]
        
        fed_count = sum(1 for l in today_logs if 'feed' in l.get('action', ''))
        walked_count = sum(1 for l in today_logs if 'walk' in l.get('action', ''))
        health_events = [l['note'] for l in today_logs if 'health' in l.get('action', '')]

        summary_lines.append(f"🐾 {pet['name']} ({pet['species']}):")
        summary_lines.append(f"   Кормлений: {fed_count}, Прогулок: {walked_count}")
        if health_events:
            summary_lines.append(f"   Здоровье: {'; '.join(health_events)}")

    return "\n".join(summary_lines)
