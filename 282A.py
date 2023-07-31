x = 0

n = int(input())

i = 0

instructions = []

while i < n:
    instructions.append(input())
    i = i + 1

i = 0

while i < len(instructions):
    test = instructions[i]
    if test.find('++') != -1:
        x = x + 1
    if test.find('--') != -1:
        x = x - 1
    i = i + 1

print(x)
