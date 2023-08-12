t = int(input())
j = 0

while j < t:

    n = int(input())
    arrayIn = input().split()

    i = 0

    b = []
    c = []



    while i < n:
        arrayIn[i] = int(arrayIn[i])

        i = i + 1


    countMin = arrayIn.count(min(arrayIn))
    i = 0

    while i < countMin:
        a = min(arrayIn)
        b.append(a)
        arrayIn[arrayIn.index(a)] = a + 1
        i = i + 1

    i = 0
    while i < countMin:
        arrayIn[arrayIn.index(a + 1)] = 0
        i = i + 1

    countMax = arrayIn.count(max(arrayIn))
    i = 0

    while i < countMax:
        a = max(arrayIn)
        c.append(a)
        arrayIn[arrayIn.index(a)] = 0
        i = i + 1

    i = 0


    while i < n:
        if arrayIn[i] != 0:
            c.append(arrayIn[i])
            arrayIn[i] = 0

        i = i + 1


    if c.count(0) == len(c):
        print(-1)
    else:
        print("{} {}".format(len(b), len(c)))
        print(*b, sep = " ")
        print(*c, sep = " ")

    j = j + 1

# 3
# 2 2 2

# -1

# 5
# 1 2 3 4 5

# 1 3 5
# 2 4

# 3
# 1 3 5

# 1
# 3 5

# 7
# 1 7 7 2 9 1 4

# 1 1
# 2 4 7 7 9

# 5
# 4 8 12 12 4

# 4 8 4
# 12 12
