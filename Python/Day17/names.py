nameStr = 'Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vansh Rajat Sagar '

nameList = nameStr.split()
repeatedNames = []

for x in range(len(nameList)):
    for j in range(x + 1, len(nameList)):
        if nameList[x] == nameList[j] and nameList[x] not in repeatedNames:
            repeatedNames.append(nameList[x])

print(repeatedNames)
