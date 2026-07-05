# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: PetCare
def archive_old_records(cutoff_date=None):
    if cutoff_date is None:
        from datetime import datetime, timedelta
        cutoff_date = datetime.now() - timedelta(days=30)
    
    archived_count = 0
    for record in records_list:
        if isinstance(record['timestamp'], str):
            ts_dt = datetime.fromisoformat(record['timestamp'].replace('Z', '+00:00'))
        else:
            ts_dt = record['timestamp']
        
        if ts_dt < cutoff_date and not record.get('_archived'):
            record['_archived'] = True
            archived_count += 1
    
    return archived_count
