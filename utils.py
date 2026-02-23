import shutil
import os

class BackupManager:
    def backup_data(self):
        os.makedirs("data/backup", exist_ok=True)
        shutil.copy("data/notes.json", "data/backup/notes_backup.json")
        shutil.copy("data/calculations.csv", "data/backup/calculations_backup.csv")
        print("Backup Created!")

    def restore_data(self):
        shutil.copy("data/backup/notes_backup.json", "data/notes.json")
        shutil.copy("data/backup/calculations_backup.csv", "data/calculations.csv")
        print("Data Restored!")