def multiply(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 0
    elif a == 1:
        return b
    elif b == 1:
        return a
    elif a < 0:
        return - (b - multiply(b, a+1))
    else:
        return multiply(b, a-1) + b


print(multiply(1200000, 365))
