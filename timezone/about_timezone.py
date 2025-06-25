from datetime import datetime
from datetime import timezone
import time

timestamp_utc = datetime.now(timezone.utc)
localtime_offset = timestamp_utc.astimezone().strftime("%z")
localtime_name = timestamp_utc.astimezone().strftime("%Z")

print(f"{timestamp_utc=}")
print(f"{localtime_offset=}")
print(f"{localtime_name=}")
