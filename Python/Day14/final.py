def printComb(sList):
    if len(sList) == 0:
        return []

    if len(sList) == 1:
        return[sList]

    j = []

    for i in range(len(sList)):
        m = sList[i]
        remList = sList[:i] + sList[i+1:]

        for p in printComb(remList):
            j.append([m]+p)

    return j


students = ['Ram', 'Anuj', 'Deepak', 'Ravi']
for comb in printComb(students):
    print(comb)
