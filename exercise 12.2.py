# Convert string into a datetime object

from datetime import datetime

date_string="Feb 25 2020 4:20PM"

date_time_obj=datetime.strptime(date_string,"%b %d %Y %H:%M%p")

print(date_time_obj)