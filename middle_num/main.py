def stredne_cislo():
    n = int(input("Zadaj cislo: "))
    pocet_cifier = 0
    temp_cislo = n
    while temp_cislo != 0:
        temp_cislo //= 10
        pocet_cifier += 1

    temp_cislo = n
    middle_index = pocet_cifier//2

    if pocet_cifier % 2 == 1:
        for i in range(pocet_cifier, middle_index,):
            temp_cislo //= 10
            middle_digit = temp_cislo % 10
    print(middle_digit)
    return middle_digit


stredne_cislo()
