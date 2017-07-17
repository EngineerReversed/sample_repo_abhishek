from datetime import datetime, timedelta
y = int(raw_input("Enter hour: "))
m = int(raw_input("Enter minute: "))
d = int(raw_input("Enter a second: "))

date = datetime.datetime.time(y,m,d)
print(date)
print(datetime.datetime(date) - timedelta(hours=9, minutes=30))
