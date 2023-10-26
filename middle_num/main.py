def stredne_cislo():
    n = int(input("Zadaj cislo: "))
    pocet_cifier = 0
    temp_cislo = 0
    while temp_cislo != 0:
        temp_cislo //= 10
        pocet_cifier += 1

    temp_cislo = n

    if pocet_cifier % 2 == 1:
        stredna_cifra = temp_cislo//10
        print(stredna_cifra)


stredne_cislo()
