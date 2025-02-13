from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Now:", current_date.strftime("%Y-%m-%d"))
print("5 days ago:", new_date.strftime("%Y-%m-%d"))
