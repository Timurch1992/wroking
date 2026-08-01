# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: PetCare
def repair_data(data):
    """Проверка целостности данных и ремонт простых проблем."""
    if not isinstance(data, dict) or 'pets' not in data:
        return {'error': 'Некорректный формат файла', 'data': {}}
    
    for pet_id, pet in data['pets'].items():
        if not isinstance(pet, dict):
            continue
        
        # Проверка обязательных полей
        required_fields = ['name', 'species']
        for field in required_fields:
            if field not in pet or not pet[field]:
                pet[field] = f'Неизвестный {field}'
        
        # Проверка дат
        date_fields = ['last_feeding_date', 'last_health_check_date', 
                      'last_walk_date']
        for field in date_fields:
            if field in pet and isinstance(pet[field], str):
                try:
                    datetime.strptime(pet[field], '%Y-%m-%d')
                except ValueError:
                    pet[field] = None
        
        # Проверка списка прививок
        if 'vaccines' not in pet or not isinstance(pet['vaccines'], list):
            pet['vaccines'] = []
        
        # Проверка списка прогулок
        if 'walks' not in pet or not isinstance(pet['walks'], list):
            pet['walks'] = []

    return data
