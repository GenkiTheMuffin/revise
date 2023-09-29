num = int(input("Zadaj cislo: "))
power = 1
sol = 0
while num > 0:
    b = num % 2
    sol = sol + b * power
    power = power * 10
    num = num // 2
print(sol)
