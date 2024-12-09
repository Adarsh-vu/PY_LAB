numbers=[-8,12,10,-15,-18,6,14]
pos=[num for num in numbers if num>0]
print(f"The positive numbers in the list {numbers} are: {pos} ")

n=5
squares=[numbs**2 for numbs in range(1,n+1)]
print(f"The squares of first {n} numbers is {squares}")

words="PlaneteryDevastation"
vow={word for word in words if word in['a','e','i','o','u']}
print(f"The list of vowels in the word '{words}' are:{sorted(vow)}")


w="Anxious"
ord=[ord(char) for char  in w] #numerical representation of charcters in ASCII
print(f"The ordinal values of each characters of the word {w} are:{ord}")

