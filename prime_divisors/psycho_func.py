def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


n = int(input("Zadaj cislo: "))
delitele = []

for i in range(2, n + 1):
    if n % i == 0 and is_prime(i):
        delitele.append(i)

print(delitele)
