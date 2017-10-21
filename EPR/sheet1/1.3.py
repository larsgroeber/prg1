import datetime

date_string = input("Please enter a date in the format 'DDMMYYYY': ")

day = int(date_string[:2])
month = int(date_string[2:4])
year = int(date_string[4:])

date = datetime.date(year, month, day)

christmas_year = year
if month == 12 and day > 24:
    christmas_year = christmas_year + 1

christmas = datetime.date(christmas_year, 12, 24)

print("There are still {} day(s) left until christmas.".format((christmas - date).days))