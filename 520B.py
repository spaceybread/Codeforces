import math

inner = input().split()
start = int(inner[0])
stop = int(inner[1])

i = 0
while True:
    if start > stop:
        print(int(i + (start - stop)))
        exit()
    elif start < stop:
        if stop % 2 == 0:
            stop = stop/2
        else:
            stop = stop + 1

        i = i + 1

    else:
        print(int(i))
        exit()
