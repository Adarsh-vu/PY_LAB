mydict={'apple':8,'peach':6,'orange':4,'strawberry':2}
asc_key=sorted(mydict.keys())
print("Dictionary of Ascending order of keys",asc_key)
desc_key=sorted(mydict.keys(),reverse=True)
print("Dictionary of Descending order of keys",desc_key)


asc_val=sorted(mydict.values())
print("Dictionary of Ascending order of Values",asc_val)
desc_val=sorted(mydict.values(),reverse=True)
print("Dictionary of Descending order of Values",desc_val)

