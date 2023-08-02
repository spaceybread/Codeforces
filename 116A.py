stops = int(input())

i = 0
stationOut = []
stationIn = []

while i < stops:
    spl = input().split()
    stationOut.append(int(spl[0]))
    stationIn.append(int(spl[1]))
    i = i + 1

i = 0
carryOver = [0, ]

while i < stops:
    carryOver.append(stationIn[i] - stationOut[i] + carryOver[i])
    i = i + 1

print(max(carryOver))
