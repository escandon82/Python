# Print a date in a the following format

from datetime import datetime

given_date = datetime(2020, 2, 25)

given_date.strftime("%A %d %b %Y")