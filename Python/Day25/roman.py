def int_to_Roman(num):
    numbers = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    roman = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // numbers[i]):
            roman_num += roman[i]
            num -= numbers[i]
        i += 1
    return roman_num
print(int_to_Roman(999))
