num = int(input("Zadaj cislo: "))
power = 1
sol = 0
while num > 0:
    b = num % 10  # get remainder after dividing by 2 (get  numeral)
    sol = (
        sol + b * power
    )  # add numeral to solution (power of ten since we need it backwards)
    power = power * 2  # next power of 10
    num = num // 10  #
print(sol)
