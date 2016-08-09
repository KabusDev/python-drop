import datetime
name = raw_input("What is your name?: ")
day = raw_input("Day of your birthday?: ")
month = raw_input("Month of your birthday?: ")
year = raw_input("Year of your birthday?: ")
datetime.date(int(year),int(month),int(day))
