cells = 5000000
corpuscles = 8000


def funcnae(a, b):
    n, d = a, b
    while a != 0:
        temp = a
        a = b % a
        b = temp
    print(b)
    print(int(n/b), ':', int(d/b))


funcnae(corpuscles, cells)
