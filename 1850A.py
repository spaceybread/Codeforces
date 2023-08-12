t = int(input())
i = 0

while i < t:
    lineIn = input().split()

    if int(lineIn[0]) + int(lineIn[1]) > 9:
        print('YES')
    elif int(lineIn[0]) + int(lineIn[2]) > 9:
        print('YES')
    elif int(lineIn[1]) + int(lineIn[2]) > 9:
        print('YES')
    else:
        print('NO')

    i = i + 1
