#!/usr/bin/env python3

a = input("Please write the value of a:")
b = input("Please write the value of b:")
c = input("Please write the value of c:")
a = float(a)
b = float(b)
c = float(c)
d = b**2 - 4 * a * c
x1 = (-b + d**0.5) / (2 * a)
x2 = (-b - d**0.5) / (2 * a)
if d > 0:
    print("There are two real roots:")
    print("x1 =",x1)
    print("x2 =",x2)
elif d == 0:
    print("There is one real root:")
    print("x =",x1)

else:
    print("There are no real roots")
