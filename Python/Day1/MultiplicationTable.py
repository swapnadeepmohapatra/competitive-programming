def table(i):
    for x in range(1, 11):
        print(i, 'X', x, '=', x*i)


num = int(input('Enter the table number: '))
table(num)
