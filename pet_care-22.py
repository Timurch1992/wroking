# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: PetCare
def check_overdue_reminders(reminders, today):
    overdue = []
    for r in reminders:
        if datetime.date.today() > r["date"]:
            overdue.append(r)
    return overdue
