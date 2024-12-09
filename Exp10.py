age=int(input("Enter your age\n"))
if age<10:
	print("Your ticket rate is 7")
elif age>=10 and age<60:
	print("Your ticket rate is 10")
elif age>=60:
	print("Your ticket rate is 5")
else:
	print("Invalid entry")


