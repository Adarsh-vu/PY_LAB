import datetime as m

print("Current date and time:",m.datetime.now())
print("Current year:",m.datetime.now().year)
print("Month of the year:",m.datetime.now().strftime("%B"))
print("Week number of the year:",m.datetime.now().strftime("%U"))
print("Weekday of the week:",m.datetime.now().strftime("%A"))
print("Day of the year:",m.datetime.now().strftime("%j"))
print("Day of the month:",m.datetime.now().day)
print("Day of the week:",m.datetime.now().strftime("%A"))
