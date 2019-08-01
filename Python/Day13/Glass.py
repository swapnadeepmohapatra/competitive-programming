k = int(input('Kara Glasses: '))
r = int(input('Rani Glasses: '))

karaCost = k * 5
raniCost = r * 7

if karaCost < raniCost:
    print('Rani made more by', raniCost - karaCost, 'cents')
elif karaCost > raniCost:
    print('Kara made more by', karaCost - raniCost, 'cents')
else:
    print('Both made same money')
