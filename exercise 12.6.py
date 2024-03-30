# Add a week (7 days) and 12 hours to a given date

given_date = datetime(2020, 3, 22, 10, 0, 0)

days_to_add=7

res_date=given_date+timedelta(days_to_add,12)

print("new date will be: \n",res_date)