string=input("Enter your string\n")
if len(string)==0:
	print("Empty string provided")
else:
	f=string[0]
	newstring=f+string[1:].replace(f, '$')
print(newstring)
