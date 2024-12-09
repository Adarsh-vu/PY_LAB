lst=input("Enter the list of words comma seperated:").split(',')
maxl=max(len(word) for word in lst)
print("The length of the longest word is",maxl)


