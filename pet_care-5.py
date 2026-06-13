# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: PetCare
def delete_record(record_id, record_type):
    if not record_id:
        print("Ошибка: ID записи отсутствует.")
        return False
    try:
        key = f"{record_type}:{record_id}"
        records[key] = None
        remaining_count = sum(1 for v in records.values() if v is not None)
        print(f"Запись {record_type} #{record_id} удалена. Осталось записей: {remaining_count}")
        return True
    except KeyError:
        print(f"Ошибка: Запись {record_type} #{record_id} не найдена.")
        return False

def get_records_summary():
    active = [k for k, v in records.items() if v is not None]
    total_count = len(active)
    if not total_count:
        print("Список записей пуст.")
        return
    grouped = {}
    for key in active:
        parts = key.split(':')
        rec_type, rec_id = parts[0], int(parts[1])
        if rec_type not in grouped:
            grouped[rec_type] = []
        grouped[rec_type].append(rec_id)
    print("Активные записи:")
    for rec_type, ids in sorted(grouped.items()):
        print(f"  {rec_type}: {ids}")
