#========QUADRATIC EQAUTION solver========

#made by- Israr Alam

from math import sqrt

print("a = ",end="")
a = float(input())

print("b = ",end="")
b = float(input())

print("c = ",end="")
c = float(input())

d = b*b-4*a*c #discriminant


if d>0:
    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)

    print("Alpha =",x1,"Beta =",x2)
    print("Real and different roots")

elif d==0:
    x3 = (-b)/(2*a)

    print("Alpha =",x3,"Beta =",x3)
    print("Real and same roots")

else:
    print("No roots")