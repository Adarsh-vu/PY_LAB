num=input("Enter the number")
rev=num[::-1]
if num==rev:
	print(f"{num} is a palindrome number")
else:
	print(f"{num} is not a palindrome number")
