# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: PetCare
def calculate_weekly_stats(records, start_date):
    from datetime import timedelta, date
    week_start = start_date - timedelta(days=start_date.weekday())
    week_end = week_start + timedelta(weeks=1)
    
    filtered_records = [r for r in records if week_start <= r['date'] < week_end]
    
    feedings = sum(1 for r in filtered_records if r.get('type') == 'feeding')
    walks = sum(1 for r in filtered_records if r.get('type') == 'walk')
    health_checks = [r for r in filtered_records if r.get('type') == 'health']
    
    total_weight = sum(r.get('weight', 0) for r in filtered_records if r.get('type') == 'feeding' or r.get('type') == 'health')
    avg_weight = total_weight / len(filtered_records) if filtered_records else 0
    
    return {
        'start_date': week_start,
        'end_date': week_end,
        'feedings_count': feedings,
        'walks_count': walks,
        'health_checks_count': len(health_checks),
        'avg_weight_kg': round(avg_weight, 2) if filtered_records else None
    }
