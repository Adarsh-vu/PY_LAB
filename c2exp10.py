lst1=input("Enter the List of integers:").split(',')
m_list=[]

for num in lst1:
        num=int(num.strip())
        if num%2!=0:
                m_list.append(num)
print("Modified List:",m_list)
