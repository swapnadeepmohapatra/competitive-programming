a = int(input('Enter a number'))
b = int(input('Enter another number'))

sums = a + b
product = a * b

if (a > b):
    diff = a - b
    mina = b
    maxa = a
elif(a < b):
    diff = b - a
    mina = a
    maxa = b

avg = (a + b)/2

print('Sum: ', sums)
print('Product: ', product)
print('Difference: ', diff)
print('Average: ', avg)
print('Minimum: ', mina)
print('Maximum: ', maxa)
