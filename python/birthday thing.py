import datetime
name=input("What is your name?: ")
day=input("Day of your birthday?: ")
month=input("Month of your birthday?: ")
year=input("Year of your birthday?: ")
print (name,datetime.date(int(year),int(month),int(day)))
