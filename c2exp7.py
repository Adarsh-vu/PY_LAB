lst1=input("Enter the list of colors for List 1:")
lst2=input("Enter the list of colors for List 2:")
set1=set(lst1.split(','))
set2=set(lst2.split(','))
difference=set1-set2
difference_list=sorted(difference)
diff_string=','.join(difference_list)
print("Colors from List 1 that are not in List 2 :",diff_string)
