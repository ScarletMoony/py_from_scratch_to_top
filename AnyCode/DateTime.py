from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import locale

d1 = date(2000, 3, 12)

print(d1.year, d1.month, d1.day)

t1 = time(20, 22, 21)

print(t1.hour, t1.minute, t1.second)

print(d1.max, d1.min, t1.max, t1.min)

dt = datetime(2000, 7, 20, 18, 19, 45)

print(dt)

print(dt.date().year, dt.time().hour)

print(dt.max, dt.min)

print(datetime.now())

now = datetime.now()

new_dt = now.replace(year=2018)

print(now)
print(new_dt)

dt = datetime.strptime("30/08/2018", "%d/%m/%Y")
print(dt)

dt = datetime.strptime("29/03/2018 10:40", "%d/%m/%Y %H:%M")

print(dt)

dt = datetime.strptime("06-28-2018 9:20", "%m-%d-%Y %H:%M")
print(dt)

now1 = datetime.now()

print(now.strftime('%Y-%m-%d (%a)'))

print(now.strftime('%Y-%B-%D (%A)'))

locale.setlocale(locale.LC_ALL, "")

now2 = datetime.now()

print(now.strftime('%Y-%m-%d (%a)'))

print(now.strftime('%Y %d %B (%A)'))
