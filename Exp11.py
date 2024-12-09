import math
a=float(input("Enter the value of a\n"))
b=float(input("Enter the value of b\n"))
c=float(input("Enter the value of c\n"))
d=(b*b)-(4*a*c)

if d==0:
	root=-b/2*a
	print(f"Real and equal roots:{root}")
elif d>0:
	ans1=(-b-math.sqrt(d))/(2*a)
	ans2=(-b+math.sqrt(d))/(2*a)
	print(f"Real and distinct roots: {ans1} and {ans2}")
else:
	r=-b/2*a
	i=math.sqrt(abs(d))//2*a
	print(f"Complex and distinct roots {r} and {i}j")

