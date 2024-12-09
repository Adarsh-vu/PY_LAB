def isPrime(num):
	count=0
	for i in range (1,num+1):
		if num%i == 0:
			count+=1
	if count>2:
		return 0
	else:
		return 1

num=int(input("Enter the limit:"))
ls=[]
primel=[]

for n in range(2,num+1):
	ls.append(n)
for n in ls:
	if isPrime(n)==1:
		primel.append(n)
print(primel[::2])
