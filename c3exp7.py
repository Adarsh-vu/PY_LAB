limit=int(input("Enter the limit"))
sum=0
for num in range (1,limit):
	if num%6==0 and num%4!=0:
		sum=sum+num
print("Sum of integers that are divisible by 6 but not by 4 are:",sum)
