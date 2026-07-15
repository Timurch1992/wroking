# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: PetCare
import datetime

def parse_date(date_str):
    """Парсит строку даты в формат ДД.ММ.ГГГГ, выводит понятную ошибку при некорректном формате."""
    try:
        return datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
    except ValueError as e:
        raise ValueError(f"Неверный формат даты '{date_str}'. Используйте формат ДД.ММ.ГГГГ (например, 15.03.2024).") from e

def parse_datetime(date_str):
    """Парсит строку даты-времени в формате ДД.ММ.ГГГГ ЧЧ:ММ, выводит понятную ошибку."""
    try:
        return datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M").datetime()
    except ValueError as e:
        raise ValueError(f"Неверный формат даты '{date_str}'. Используйте формат ДД.ММ.ГГГГ ЧЧ:ММ (например, 15.03.2024 18:30).") from e
