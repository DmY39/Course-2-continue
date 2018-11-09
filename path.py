import datetime
d = datetime.datetime.strptime(input(), "%Y %m %d")
a = datetime.timedelta(int(input()))
c = d + a
print(c.year, c.month, c.day)