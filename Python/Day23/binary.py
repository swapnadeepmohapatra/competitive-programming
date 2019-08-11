def Reverse(lst):
    l = [ele for ele in reversed(lst)]
    new = ""
    for i in l:
        new += i
    return new


def convert(n):
    lol = []
    while(int(n) / 2 != 0):
        lol.append(str(n % 2))
        n = int(n/2)
    print((Reverse(lol)))


num = int(input('Enter the Decimal : '))
convert(num)
