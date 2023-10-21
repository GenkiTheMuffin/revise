n = int(input("Zadaj cislo: "))
pocet_delitelov = 0
delitele = []

for i in range(1, n+1):
    if n % i == 0:
        pocet_delitelov += 1
        delitele.append(i)

print(delitele)
print(pocet_delitelov)
