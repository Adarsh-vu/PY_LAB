number=int(input("Enter a number:"))
og_num=number
sum_pow=0
num_digit=len(str(number))
while number>0:
	digit=number%10
	sum_pow+=digit**num_digit
	number//=10
if og_num==sum_pow:
	print(f"{og_num} is an Armstrong")
else:
	print(f"{og_num} is not an Armstrong number")
