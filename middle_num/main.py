def middle_num():
    number = int(input("Enter a number: "))
    temp_number = number
    numeral_count = 0
    while temp_number != 0:
        temp_number //= 10
        numeral_count += 1
    temp_number = number
    middle_index = numeral_count // 2
    for _ in range(numeral_count - middle_index - 1):
        temp_number //= 10
    middle_digit = temp_number % 10
    print(middle_digit)


middle_num()
