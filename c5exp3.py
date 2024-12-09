import datetime as d

today = d.date.today()
yesterday = today - d.timedelta(days = 1)
tomorrow = today + d.timedelta(days = 1)

print(f"Yesterday : {yesterday}\nToday : {today}\n")
