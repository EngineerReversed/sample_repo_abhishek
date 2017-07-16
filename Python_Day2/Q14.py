import datetime
y = raw_input("Enter a year: ")
m = raw_input("Enter a month: ")
d = raw_input("Enter a day: ")

date = y+m+d
print(datetime.datetime.strptime(date,'%Y%m%d').date()+datetime.timedelta(days=1))
