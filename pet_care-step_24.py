# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: PetCare
def show_record(record):
    """Выводит одну запись в компактном виде."""
    if not record:
        return
    r = record.get("record", {})
    print(f"[{r.get('type','?')}] ID:{r.get('id')} | Дата:{r.get('date','?')}")
    for k, v in r.items():
        if k in ("id","date","type"): continue
        try:
            val = v
            if isinstance(val, bool): val = "да" if val else "нет"
            elif isinstance(val, (int,float)) and not isinstance(v, str): val = f"{val:.1f}"
            print(f"  {k}={val}")
        except Exception:
            pass
