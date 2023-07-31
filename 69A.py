coordStrings = []
 
n = int(input())
 
i = 0
while i < n:
    coordStrings.append(input())
    i = i + 1
 
coord = []
 
i = 0
while i < n:
    coord.append(coordStrings[i].split())
    i = i + 1
 
xVal = []
yVal = []
zVal = []
 
i = 0
while i < n:
    testList = coord[i]
    xVal.append(int(testList[0]))
    yVal.append(int(testList[1]))
    zVal.append(int(testList[2]))
    i = i + 1
 
i = 0
xSum = 0
ySum = 0
zSum = 0
 
while i < n:
    xSum = xSum + xVal[i]
    ySum = ySum + yVal[i]
    zSum = zSum + zVal[i]
    i = i + 1
 
if xSum == 0 and ySum == 0 and zSum == 0:
    print('YES')
else:
    print('NO')
