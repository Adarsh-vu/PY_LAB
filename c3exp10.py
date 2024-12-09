number=int(input("Enter a number for finding the factor:"))
factor=1
print(f"Factor of the {number} are:")
while factor<=number:
	if number%factor==0:
		print(factor)
	factor+=1
