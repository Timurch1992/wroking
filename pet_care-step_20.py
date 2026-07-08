# === Stage 20: Добавь восстановление записей из архива ===
# Project: PetCare
def restore_from_archive(archive_path):
    if not os.path.exists(archive_path):
        print(f"Файл архива '{archive_path}' не найден.")
        return 0
    
    records = []
    with open(archive_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|||')
            if len(parts) == 5:
                records.append({
                    'type': parts[0].strip(),
                    'date': parts[1].strip(),
                    'pet_name': parts[2].strip(),
                    'details': parts[3].strip(),
                    'note': parts[4].strip() if len(parts) > 5 else ''
                })
    
    print(f"Восстановлено {len(records)} записей из архива.")
    return records

archive_path = "pets_archive.txt"
restored_records = restore_from_archive(archive_path)
if restored_records:
    for rec in restored_records:
        if rec['type'] == 'feeding':
            print(f"{rec['date']} - Кормление '{rec['pet_name']}': {rec['details']}")
        elif rec['type'] == 'health':
            print(f"{rec['date']} - Здоровье '{rec['pet_name']}': {rec['note']}")
