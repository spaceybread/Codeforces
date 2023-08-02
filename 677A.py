firstLine = input().split()
n = int(firstLine[0])
h = int(firstLine[1])

secondLine = input().split()
i = 0
heights = []

while i < len(secondLine):
    heights.append(int(secondLine[i]))
    i = i + 1

width = 0
i = 0

while i < len(heights):
    if heights[i] > h:
        width = width + 2
    else:
        width = width + 1
    i = i + 1

print(width)
