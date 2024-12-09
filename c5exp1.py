import calendar

n=-int(input("Enter the year: "))

if calendar.isleap(n):
	print(f"The year:{n} is a leap year")

else:
	print(f"The year:{n} is not a leap year")

