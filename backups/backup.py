import os
import shutil 
from datetime import datetime, timedelta


BACKUP_DIR = "backups"
ARCHIVE_DIR = os.path.join(BACKUP_DIR, "old_backups")
REPORT_FILE = "backup_report.txt"

os.makedirs(ARCHIVE_DIR, exist_ok=True)

today = datetime.now()
archive_threshold = today - timedelta(days=7)
delete_threshold = today - timedelta(days=30)

report_lines = []

for file in os.listdir(BACKUP_DIR):
    if not file.startswith("backup_") or not file.endswith(".zip"):
        continue

    file_path = os.path.join(BACKUP_DIR, file)

    if os.path.isdir(file_path):
        continue

    try:
        date_str = file.replace("backup_", "").replace(".zip", "")
        file_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        continue

    if file_date < delete_threshold:
        os.remove(file_path)
        report_lines.append(f"Deleted: {file}")

    elif file_date < archive_threshold:
        shutil.move(file_path, os.path.join(ARCHIVE_DIR, file))
        report_lines.append(f"Archived: {file}")

    else:
        report_lines.append(f"Kept: {file}")

with open(REPORT_FILE, "w") as report:
    for line in report_lines:
        report.write(line + "\n")

for line in report_lines:
    print(line)

print(f"\nReport saved to {REPORT_FILE}")
