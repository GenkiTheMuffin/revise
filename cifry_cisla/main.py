n = int(input("Zadaj cislo: "))
a = 0
while n > 0:
    a += n % 10
    n = n // 10

print(f"Cislo ma sucet cifier {a}")
