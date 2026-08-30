# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: PetCare
def dry_run_mode(active=False):
    global _dry_run
    _dry_run = active
    print(f"[PetCare] Dry-run mode: {'ON' if active else 'OFF'}")
    return _dry_run

def _execute_action(action, **kwargs):
    if _dry_run:
        print(f"[DRY-RUN] {action}: {kwargs}")
        return None
    return action(**kwargs)
