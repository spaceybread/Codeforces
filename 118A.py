toProcString = (input().lower())
i = 0
toProc = []

while i < len(toProcString):
    toProc.append(toProcString[i])
    i = i + 1

cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n","p", "q", "r", "s", "t", "v", "w", "x", "z"]

i = 0
outStringList = []

while i < len(toProc):
    j = 0
    while j < len(cons):
        if toProc[i] == cons[j]:
             outStringList.append('.')
             outStringList.append(cons[j])
        j = j + 1
    i = i + 1

print(''.join(outStringList))
