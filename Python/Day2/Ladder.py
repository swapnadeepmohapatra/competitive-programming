for x in range(1, 10):
    k = 10-x
    if k % 2 == 0:
        for z in range(1, k):
            print(' ', end='')
        for y in range(1, x):
            print('*', end='')
        for y in range(1, x):
            print('*', end='')
    else:
        for z in range(1, k+1):
            print(' ', end='')
        for y in range(1, x-1):
            print('*', end='')
        for y in range(1, x-1):
            print('*', end='')
    print(' ')
