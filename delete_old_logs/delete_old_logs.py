from pathlib import Path
from datetime import datetime
from datetime import timedelta

logs_folder = Path("/var/lib/pgsql/data/log")

# find all log files in folder
log_files = logs_folder.glob("*.log")

#get currentdate 5 days ago
five_days_ago = datetime.now() - timedelta(days=2)

#delete all files older than 5 days ago
for log_file in log_files:
    print(f"Checking {log_file}")
    if log_file.stat().st_mtime < five_days_ago.timestamp():
        log_file.unlink()
        print(f"\tDeleted {log_file}")
