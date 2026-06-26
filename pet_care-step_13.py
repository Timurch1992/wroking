# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: PetCare
def search_records(query, fields=None):
    if not query: return []
    q = query.lower()
    if fields is None: fields = ['name', 'breed', 'notes']
    results = [r for r in records if any(q in str(r.get(f, '')).lower() for f in fields)]
    return sorted(results, key=lambda x: (x['date'], x['type']))
