for x in range(1, 11):
    n = 11
    if x % 2 != 0:
        k = x+1
    else:
        k = x
    for g in range(k, n):
        if g >= k:
            print(end=" ")
    for j in range(0, k):
        if j == k-1:
            print('*')
        else:
            print('*', end=" ")
