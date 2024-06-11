import time
import datetime
import calendar

timestamp = datetime.datetime.now()

year = timestamp.year
month = calendar.month_name[timestamp.month][:3]
day = timestamp.day
secs = time.time()
sn = "{:e}".format(secs)
print(f"Seconds since January 1, 1970: {secs} or {sn} in scientific notation")
print(f"{month} {day} {year}")
