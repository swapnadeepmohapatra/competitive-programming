def convert(n):
    lol = ''
    while(int(n) / 2 != 0):
        lol += (str(n % 2))
        n = int(n/2)
    print(lol[::-1])


num = int(input('Enter the Decimal : '))
convert(num)
