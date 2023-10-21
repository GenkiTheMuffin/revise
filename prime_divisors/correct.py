cislo = int(input("Zadaj cislo:"))
zacCislo = cislo
pocetDelitelov = 0
delitel = 2
listDelitelov = []
while delitel <= cislo:
    if cislo % delitel == 0:
        listDelitelov.append(delitel)
        pocetDelitelov += 1
        cislo /= delitel
    else:
        delitel += 1
if delitel == zacCislo:
    print(f"{zacCislo} je prvocislo")
else:
    print(listDelitelov)
