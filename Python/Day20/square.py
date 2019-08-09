# Method 1
number = 8

square = 0
for x in range(1, number*2, 2):
    square += x

print(square)


# Method 2

sq = 0
for i in range(0, number):
    sq = sq + number

print(sq)
