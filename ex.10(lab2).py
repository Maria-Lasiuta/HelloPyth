from datetime import date,timedelta

d1 = date(int(input('year1 ')), int(input('month1 ')), int(input('day1 ')))
d2 = date(int(input('year2 ')), int(input('month2 ')), int(input('day2 ')))
day_generator = (d1 + timedelta(x + 1) for x in range((d2 - d1).days))
# generate all days from d1 to d2
print (sum(1 for day in day_generator if day.weekday() < 5)) 

