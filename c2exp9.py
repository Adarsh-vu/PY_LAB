lst1=input("Enter the list of integers:").split(',')
m_list=[]
for num in lst1:
        num=int(num.strip())
        if num>100:
                m_list.append('over')
        else:
                m_list.append(num)

print("Modified List:",m_list)
