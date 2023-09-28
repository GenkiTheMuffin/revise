#!/usr/bin/env python3

s1=int(input("zadaj stranu 1: "))
s2=int(input("zadaj stranu 2: "))
s3=int(input("zadaj stranu 3: "))

if s1 + s2 >= s3 and s1+s3 >= s2 and s2 + s3 >= s1:
    print("je to trojuholnik")
if s1 == s2 and s1==s3 and s2==s3:
    print('trojuholnik je rovnostrany')
if s1 == s2 or s2==s3 or s3==s1:
    print('trojuholnik je rovnorameny')
a, b, c = sorted([s1, s2, s3])
if a**2 + b**2 == c**2:
    print('trojuholnik je pravy')
