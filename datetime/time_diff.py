from datetime import datetime
from dateutil.parser import parse

# start time
start_time = parse("2023-02-03 11:39:24.373021+00")
end_time = parse("2023-02-07 05:11:20.856176+00")

# convert time string to datetime
t1 = start_time
print('Start time:', t1.time())

t2 = end_time
print('End time:', t2.time())

# get difference
delta = t2 - t1

# time difference in seconds
print(f"Time difference is {delta.total_seconds()} seconds")

# time difference in seconds rounded off
print(f"Time difference is {round(delta.total_seconds())} seconds rounded off")

# time difference in milliseconds
ms = delta.total_seconds() * 1000
print(f"Time difference is {ms} milliseconds")

# time difference in days
print(f"Time difference is {delta.total_seconds() / 86400} days")

# time difference in hours
print(f"Time difference is {delta.total_seconds() / 3600} hours")
