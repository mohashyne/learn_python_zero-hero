import time

# Working with date and time in Python is straightforward, thanks to its robust libraries like datetime and time. These libraries allow you to work with dates, times, and timestamps effectively.
# What is a Timestamp?

# A timestamp represents a point in time, usually given as the number of seconds (or milliseconds) since the Unix epoch (00:00:00 UTC on 1 January 1970).

# Key Modules for Date and Time

#     datetime: Provides classes for working with dates and times.
#     time: Focuses on time-related tasks like delays and formatting.
#     calendar: Handles calendar-related tasks (optional but useful).

# print(time.time()) # 1734866007.951333


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start

print(f"Time taken: {duration} seconds")  # 0.000999999
