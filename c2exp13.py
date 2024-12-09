text=input("Enter the text line\n".lower())
words=text.split()
w_count={}

for word in words:
	if word in w_count:
		w_count[word]+=1
	else:
		w_count[word]=1


print("Word Occurrences",w_count)

