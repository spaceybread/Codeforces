n = int(input()) + 1
a = list(map(int, input().split()))

s = sum(a)

c = 0

for i in range(1, 6):
    if ((s + i) % n) != 1: c += 1

print(c)
