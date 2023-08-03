import math

numberIn = input()

i = 0

numberList = []

while i < len(numberIn):
    a = int(numberIn[i])
    if a > 4:
        if a == 9 and i == 0:
            pass
        else:
            a = 9 - a
    numberList.append(str(a))
    i = i + 1

print("".join(numberList))
