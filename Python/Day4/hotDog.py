totalHotDog = 400
hotDogInPackage = 8

i = 0
while totalHotDog > 0:
    totalHotDog = totalHotDog - hotDogInPackage
    i = i + 1

print('Total packages are: ', i)
