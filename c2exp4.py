string=input("Enter your string:")
s={}
for i in string:
	if i in s:
		s[i]+=1
	else:
		s[i]=1

print(s)
