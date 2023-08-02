weightList = input().split()
a = int(weightList[0])
b = int(weightList[1])

i = 0

while True:
    i = i + 1
    a = a*3
    b = b*2
    if a > b:
        print(i)
        exit()
