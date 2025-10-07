from datetime import datetime

# set first_date to Jan 1 1970
first_date = datetime(1970, 1, 1)
# get current date
date = datetime.now()
# get seconds from Jan 1 1970 to present 
sec = (date - first_date).total_seconds()
# convert seconds to scientific notation with format
# - .2 => show 2 digits after decimals
# - e  => convert to scientific notation
scientific_notation = f"{sec:.2e}"
# add commas to seconds
# - ,  => adds commas as thousands separator
# - .6 => make sure I always have 6 decimals
# - f  => to keep the number as a fixed-point decimal
comma_sec = f"{sec:,.6f}"

print(f"Seconds since January 1, 1970: {comma_sec} or {scientific_notation} in scientific notation")
# date:%x is the same as date.strftime("%x")
print(f"{date:%b} {date:%d} {date:%Y}")