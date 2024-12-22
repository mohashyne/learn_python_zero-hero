# import datetime
from datetime import datetime, timedelta
import time

# Formatting Date and Time
# Use strftime for formatting and strptime for parsing strings.
# Format Code	Description	Example
# %Y	Year (4 digits)	2024
# %m	Month (2 digits)	12
# %d	Day (2 digits)	21
# %H	Hour (24-hour)	14
# %M	Minute	30
# %S	Second	45
# %p	AM/PM	PM


# A timedelta in Python is an object that represents the difference (duration) between two dates, times, or both. It is part of the datetime module and is commonly used for adding or subtracting time intervals, calculating durations, and working with dates and times in Python.
# Creating a timedelta

# You can create a timedelta object by specifying any combination of the following arguments:

#     days
#     seconds
#     microseconds
#     milliseconds
#     minutes
#     hours
#     weeks




d1 = datetime(2020, 1, 1)
d2 = datetime.now()


duration = d2 - d1
print(duration) # 1817 days, 14:03:35.574313

print(duration.days) # 1817
print(duration.seconds) # 50635
print(duration.total_seconds()) # 157039587.620168


d3 = datetime(2020, 1, 1) + timedelta(days=1, seconds=1)
print(d3) # 2020-01-02 00:00:01
print(d1) # 2020-01-01 00:00:00



#++++++++++++++
# Create a timedelta object
delta = timedelta(days=5, hours=3, minutes=30)
print(delta)  # Output: 5 days, 3:30:00

# Common Use Cases of timedelta
# 1. Adding/Subtracting Time
# You can use timedelta to perform arithmetic with datetime objects.

from datetime import datetime, timedelta

# Current time
now = datetime.now()
print("Now:", now)

# Add 5 days
future_date = now + timedelta(days=5)
print("5 Days Later:", future_date)

# Subtract 2 hours
past_date = now - timedelta(hours=2)
print("2 Hours Ago:", past_date)


# Practical Example: Deadline Reminder

from datetime import datetime, timedelta

# Set a deadline
deadline = datetime(2025, 1, 1, 12, 0)

# Calculate time remaining
now = datetime.now()
remaining_time = deadline - now
print(f"Time until deadline: {remaining_time.days} days, {remaining_time.seconds // 3600} hours")

# This makes timedelta a versatile tool for managing and calculating durations in Python.