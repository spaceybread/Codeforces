n = int(input())
i = 0

while i < n:
    lineIn = input().split()

    slices = int(lineIn[0])
    things = int(lineIn[1]) + int(lineIn[2])

    if slices > things:
        print(2*things + 1)
    elif slices == things:
        print(2*things - 1)
    elif slices < things:
        print(2*slices - 1)

    i = i + 1
