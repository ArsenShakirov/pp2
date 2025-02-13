from datetime import datetime

now = datetime.now().replace(microsecond=0)

print("Datetime without microseconds:", now)
