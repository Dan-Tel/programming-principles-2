import datetime

# Write a Python program to subtract five days from current date.
def five_days_ago():
  today = datetime.datetime.today()
  five_days = datetime.timedelta(days=5)
  print(today - five_days)

# Write a Python program to print yesterday, today, tomorrow.
def yesterday_today_tomorrow():
  today = datetime.datetime.today()
  one_day = datetime.timedelta(days=1)
  print(today - one_day)
  print(today)
  print(today + one_day)

# Write a Python program to drop microseconds from datetime.
def drop_microseconds(date):
  print(date.replace(microsecond=0))

# Write a Python program to calculate two date difference in seconds.
def difference_in_seconds(date_1, date_2):
  print(abs(date_1 - date_2).total_seconds())