# import datetime
from datetime import datetime
import time

# dt = datetime.datetime(2018, 1, 1) # this look somehow ugly, instead we import the whole of the datetime module
# from datetime import datetime

today = datetime.now()
print(today)

dt = datetime(2018, 1, 1)
print(dt)  # 2018-01-01 00:00:00

# parsing or converting datetime strings, useful when we get input from a user or string and want to convert datetime object

d1 = datetime.strptime("2020/01/01", "%Y/%m/%d")
d2 = datetime.strptime("2020-01-01", "%Y-%m-%d")
print("convert string datetime object:", d1)
print("Time2:", d2)

print(f"{d1.year}/{d1.month}")
# convert datetime  object to  string , this is the opposite of strptime
print("convert datetime object to string:",  dt.strftime("%Y/%m"))


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



d3 = datetime.fromtimestamp(time.time())
print("Time3:", d3)


print(d1 > d2) # False