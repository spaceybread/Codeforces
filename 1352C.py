import math
vals = int(input())
i = 0
inputList = []
while i < vals:
    inputList.append(input())
    i = i + 1

i = 0

while i < vals:
    valIn = inputList[i].split()
    n = int(valIn[0])
    k = int(valIn[1])

    x = int(k/(n - 1))

    r = k - x*(n-1)

    if r == 0:
        print(x*n - 1)
    else:
        print(x*n + r)

    i = i + 1
