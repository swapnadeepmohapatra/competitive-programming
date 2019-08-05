import itertools

students = ['Ram', 'Anuj', 'Deepak', 'Ravi']

temp = itertools.permutations(students)

for i in list(temp):
    print(i)
