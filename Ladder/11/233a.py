n = int(input())

if n % 2 == 1: 
    print(-1)
    exit()


o = []

for i in range(1, n + 1, 2):
    seg = [str(i + 1), str(i)]
    o += seg

print(*o)
