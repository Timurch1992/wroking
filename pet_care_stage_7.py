# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: PetCare
def sort_records(records, key='date', reverse=True):
    if not records: return []
    def parse_date(r):
        try: return datetime.fromisoformat(r['timestamp'].replace('Z', '+00:00'))
        except: return datetime.min
    def get_priority_score(r):
        p_map = {'high': 3, 'medium': 2, 'low': 1}
        return p_map.get(str(r.get('priority', 'low')).lower(), 0)
    if key == 'date':
        records.sort(key=lambda x: parse_date(x), reverse=reverse)
    elif key == 'priority':
        records.sort(key=get_priority_score, reverse=True)
    elif key == 'name':
        records.sort(key=lambda x: str(x.get('pet_name', '')).lower(), reverse=False)
    return records
