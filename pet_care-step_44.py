# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: PetCare
import shutil, os, sys
BACKUP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_backups")
def backup_data(filename="pets.json"):
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    if not os.path.exists(src):
        print(f"[Backup] Файл {filename} не найден, пропуск.")
        return
    ts = os.path.splitext(filename)[0] + "_" + time.strftime("%Y%m%d_%H%M%S")
    dst = os.path.join(BACKUP_DIR, ts + os.path.splitext(filename)[1])
    shutil.copy2(src, dst)
    print(f"[Backup] Создана резервная копия: {dst}")
