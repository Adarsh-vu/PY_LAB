def add_num(*args):
 """
 Sum of Integers
 """
 return sum(args)
list1=(map(int,input("Enter the numbers seperated by commas: ").split(",")))
print("sum = ",add_num(*list1))
