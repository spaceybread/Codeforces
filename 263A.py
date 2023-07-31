rowStrings = []

i = 0
while i < 5:
    rowStrings.append(input())
    i = i + 1

rows = []

i = 0
while i < 5:
    rows.append(rowStrings[i].split())
    i = i + 1

i = 0
j = 0
testList = []
coords = []

while i < 5:
    testList = rows[i]
    j = 0
    while j < 5:
        testVal = int(testList[j])
        if testVal == 1:
            coords.append(i)
            coords.append(j)
            break
        j = j + 1
    i = i + 1

#print(rows)
#print(coords)

steps = abs(coords[0] - 2) + abs(coords[1] - 2)
print(steps)
