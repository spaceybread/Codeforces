x, y, z = 0, 0, 0
for _ in range(int(input())):
    xi, yi, zi = map(int, input().split())
    x += xi
    y += yi
    z += zi

if x == y == z == 0: print("YES")
else: print("NO")
