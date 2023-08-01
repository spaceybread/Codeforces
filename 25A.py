n = int(input())
numStrList = input().split()

numList = []

i = 0
while i < n:
    numList.append(int(numStrList[i]))
    i = i + 1

even = 0
odd = 0

i = 0
while i < n:
    if numList[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    i = i + 1

modVal = 0

if even > odd:
    modVal = 1
else:
    modVal = 0

i = 0
while i < n:
    if numList[i] % 2 == modVal:
        print(i + 1)
        exit()
    i = i + 1
