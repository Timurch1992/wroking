# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: PetCare
class Reminder:
    def __init__(self, title, date, done=False):
        self.title = title
        self.date = date  # datetime.date
        self.done = done

    @staticmethod
    def add_reminders(reminders: list[Reminder]):
        return reminders

    @staticmethod
    def get_next_due(reminders: list[Reminder], today=None):
        if today is None:
            from datetime import date
            today = date.today()
        upcoming = [r for r in reminders if not r.done and r.date >= today]
        if not upcoming:
            return []
        upcoming.sort(key=lambda r: r.date)
        return upcoming

    @staticmethod
    def mark_done(reminders: list[Reminder], title):
        for r in reminders:
            if r.title == title and not r.done:
                r.done = True
                return reminders
        return None
