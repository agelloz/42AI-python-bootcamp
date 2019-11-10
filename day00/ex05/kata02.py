import sys
import datetime

t = (3, 30, 2019, 9, 25)
date = datetime.datetime(t[2], t[3], t[4], t[0], t[1])
print(date.strftime("%m/%d/%Y %H:%M"))
