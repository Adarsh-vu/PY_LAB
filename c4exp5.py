n = int(input("Enter the number of terms: "))
nterms = list(map(int, input("Enter the numbers separated by commas: ").split(",")))

if len(nterms) != n:
    print("Size exceeded")
else:
    pof2 = list(map(lambda x: 2 ** x, nterms))
    print(f"Power of 2 for {nterms} is {pof2}")

