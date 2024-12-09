lst1=input("Enter the integers to list 1:").split(',')
lst2=input("Enter the integers to list 2:").split(',')

lst1=[int(num.strip()) for num in lst1]
lst2=[int(num.strip()) for num in lst2]

if len(lst1)==len(lst2):
	print("The given two strings are of equal length")
else:
	print("The length of the given two strings are not equal")

if sum(lst1)==sum(lst2):
	print("The sum of the given strings are equal")

else:
	print("The sum of the given strings are not equal")

common_value=[]

for num in lst1:
	if num in lst2:
		common_value.append(num)
if not common_value:
	print("No common values exits among the lists")

else:
	print("The common values in the two list are:",common_value)

