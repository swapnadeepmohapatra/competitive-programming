# find the second highest number from the list.

if __name__ == '__main__':
    i = int(input())
    lis = list(map(int, input().strip().split()))
    z = max(lis)

    while max(lis) == z:
        lis.remove(max(lis))

    print(max(lis))