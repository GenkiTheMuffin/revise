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
        for i in range(numeral_count - middle_index - 1):
            temp_number //= 10
        middle_digit_a = temp_number % 10
        middle_digit_b = (temp_number % 100 - temp_number % 10)//10
        middle_digit = (middle_digit_a + middle_digit_b)/2
    print(middle_digit)


middle_num()
