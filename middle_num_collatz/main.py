def middle_num():
    number = int(input("Enter a number: "))
    temp_number = number
    numeral_count = 0
    while temp_number != 0:
        temp_number //= 10
        numeral_count += 1
    temp_number = number
    middle_index = numeral_count // 2
    if numeral_count % 2 != 0:
        for _ in range(numeral_count - middle_index - 1):
            temp_number //= 10
        middle_digit = temp_number % 10
    else:
        for _ in range(numeral_count - middle_index - 1):
            temp_number //= 10
        middle_digit_a = temp_number % 10
        middle_digit_b = (temp_number % 100 - temp_number % 10)//10
        middle_digit = (middle_digit_a + middle_digit_b)/2
    print(middle_digit)
    return middle_digit


def collatz(n):
    list_of_steps = []
    while n != 1:
        if n % 2 == 0:
            n /= 2
            list_of_steps.append(n)
        else:
            n = 3*n+1
            list_of_steps.append(n)

    print(list_of_steps)


middle = middle_num()
collatz(middle)
