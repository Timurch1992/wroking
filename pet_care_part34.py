# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: PetCare
TEMPLATE_REGISTRY = {
    "daily_feeding": {
        "prompt": "Введите имя питомца:",
        "fields": {"pet_name": None, "food_type": None, "amount_grams": 0},
    },
    "health_check": {
        "prompt": "Введите тип проверки (температура/вес/шерсть):",
        "fields": {"check_type": None, "value": "", "unit": ""},
    },
    "walk": {
        "prompt": "Длительность прогулки в минутах:",
        "fields": {"duration_min": 0, "weather": None},
    },
    "note": {
        "prompt": "Введите текст заметки:",
        "fields": {"text": ""},
    },
}

def get_template(name):
    if name in TEMPLATE_REGISTRY:
        return TEMPLATE_REGISTRY[name]
    raise ValueError(f"Нет шаблона '{name}'")

def fill_template(template_name, user_input):
    tmpl = get_template(template_name)
    for field in tmpl["fields"]:
        if field is None or (isinstance(user_input.get(field), str) and not user_input[field]):
            continue
        if isinstance(tmpl["fields"][field], type(None)):
            user_input[field] = input(tmpl["prompt"] + " ")
    return user_input
