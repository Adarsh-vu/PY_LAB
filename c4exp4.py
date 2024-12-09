sqr=lambda side:side*side
rect=lambda l,b:l*b
tr=lambda ba,he:0.5*ba*he
print("\nAREA OF SQUARE")
side=float(input("Enter a side Square: "))
print(f"Area is {sqr(side)}")
print("\nAREA OF RECTANGLE")
l=float(input("Enter the Length: "))
b=float(input("Enter the Breadth: "))
print(f"Area is {rect(l,b)}")
print("\nAREA OF TRIANGLE")
base=float(input("Enter the base of the triangle: "))
height=float(input("Enter the height of th triangle: "))
print(f"Area is {tr(base,height)}")
