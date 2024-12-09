def fact(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	return fact

n=int(input("Enter the no.of terms:"))
terms=list(map(lambda x:(x**x)/fact(x),range(1,n+1)))

sum=0
for num in terms:
	sum=sum+num

print(f"sum of terms={sum}")
