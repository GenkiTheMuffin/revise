n = int(input("Zadaj cislo: "))
pocet_cifry = 0
suma_cifier = 0
while n != 0:
    x = n % 10  # otrhni poslednu cifry
    n = n//10  # zmensi pocet cifier o 1 cifru
    pocet_cifry += 1
    suma_cifier += x
print(f"Sucet cifier je {suma_cifier}")
print(f"Pocet cifier je {pocet_cifry}")
