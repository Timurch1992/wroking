# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: PetCare
def export_state_to_json():
    import json
    from datetime import datetime
    data = {
        "pets": pets,
        "logs": logs,
        "settings": settings,
        "exported_at": datetime.now().isoformat()
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
