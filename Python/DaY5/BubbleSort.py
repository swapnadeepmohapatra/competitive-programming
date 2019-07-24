def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)


arr = [66, 57, 54, 53, 64, 52, 59]

sort(arr)
print('The best score is: ', arr[len(arr)-1])
