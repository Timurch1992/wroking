# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: PetCare
def load_data_from_json(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные успешно загружены из {filepath}")
        return data
    except FileNotFoundError:
        print(f"Ошибка: файл '{filepath}' не найден.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка формата JSON в файле '{filepath}': {e}")
        return {}
    except PermissionError:
        print(f"Ошибка: нет прав для чтения файла '{filepath}'.")
        return {}
