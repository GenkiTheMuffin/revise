cislo = int(input("Zadaj cislo:"))
zacCislo = cislo
opacCislo = 0
a = 0
while cislo != 0:
    opacCislo = (opacCislo*10)+(cislo % 10)
    cislo //= 10
    a += 1
if opacCislo == zacCislo:
    print(f"Cislo {zacCislo} je palindrom")
else:
    print(f"Cislo {zacCislo} nie je palindrom")
