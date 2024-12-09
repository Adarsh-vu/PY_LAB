def compare(str1,str2,n):
 if n<=0:
  raise ValueError("Number must be positive!!")
 return str1[:n]==str2[:n]

string1=input("Enter the First String: ")
string2=input("Enter the second String: ")
n=int(input("Enter the no:of Charachters: "))
print(f"Equivalence = {compare(string1,string2,n)}")
