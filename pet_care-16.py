# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: PetCare
def calculate_monthly_stats(records, month_year):
    """Генерирует сводную статистику за указанный месяц."""
    stats = {
        "total_feeding": 0,
        "feeding_count": 0,
        "health_issues": [],
        "walks_total_minutes": 0,
        "notes_count": 0,
        "active_days": set()
    }

    for record in records:
        if not isinstance(record, dict):
            continue
        
        date_str = record.get("date")
        if not date_str or len(date_str) < 7:
            continue
            
        # Формат даты YYYY-MM-DD или YYYY.MM.DD
        try:
            year = int(date_str[:4])
            month = int(date_str[5:7])
            
            if year != month_year.year or month != month_year.month:
                continue
                
            stats["active_days"].add(date_str)
            
            action = record.get("action", "").lower()
            amount = record.get("amount")
            
            if "корм" in action and amount is not None:
                stats["total_feeding"] += float(amount)
                stats["feeding_count"] += 1
            
            elif "проблема" in action or "болезнь" in action:
                issue = record.get("note", "")
                if issue:
                    stats["health_issues"].append(issue[:50]) # Храним только начало проблемы
            
            elif "прогулка" in action and amount is not None:
                try:
                    duration_mins = float(amount)
                    stats["walks_total_minutes"] += duration_mins
                except ValueError:
                    pass
                    
        except (ValueError, IndexError):
            continue

    return {k: v for k, v in stats.items() if isinstance(v, list) or not isinstance(v, set)}
