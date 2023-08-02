n = int(input())
inputNames = []

i = 0

while i < n:
    inputNames.append(input())
    i = i + 1

registerNames = []
registerCount = []

i = 0

while i < n:
    if registerNames.count(inputNames[i]) != 0:
        userIndex = registerNames.index(inputNames[i])
        userNumber = str(registerCount[userIndex])
        print("".join([inputNames[i], userNumber]))
        registerCount[userIndex] = registerCount[userIndex] + 1
    else:
        print('OK')
        registerNames.append(inputNames[i])
        registerCount.append(1)

    i = i + 1
