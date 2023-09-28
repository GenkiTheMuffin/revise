#!/usr/bin/env python3

a=int(input('Zadaj prve cislo: '))
b=int(input('Zadaj druhe cislo: '))
c=int(input('Zadaj tretie cislo: '))

if a>b:
    if a>c:
        if b>c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
else:
    if b>c:
        if a>c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        print(c,b,a)
#du 3 a 4 6 7 11
#4 ci je rovnoramenny rovno strany / pravouhly
#bonus 8


