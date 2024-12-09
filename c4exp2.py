def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	if b == 0:
		print("Division is possible when denominator is zero!!!")
	else:
		return a/b

while(True):

	print("\n 1.ADDITION \n 2.SUBSTRACTION \n 3.MULTIPLICATION \n 4.DIVISION \n 5.EXIT")
	choice=int(input("\n Enter your choice"))

	if choice >= 5:
		print("\nInvalid Choice")
		break;
	elif choice in [1,2,3,4]:
		num1=int(input("Enter the first number:"))
		num2=int(input("Enter the second number:"))
	if choice == 1:
		print(f"The sum of {num1} and {num2} is {add(num1,num2)}")

	elif choice == 2:
		print(f"The difference between {num1} and {num2} is {sub(num1,num2)}")

	elif choice == 3:
		print(f"The product of {num1} and {num2} is {mul(num1,num2)}")

	elif choice == 4:
		print(f"Result of divison = ",div(num1,num2))

	else:
		print("Invalid choice!!!")

