from collections import defaultdict

n = int(input())

mx = defaultdict(list)
my = defaultdict(list)

pts = []

for _ in range(n):
    x, y = map(int, input().split())
    
    mx[x].append(y)
    my[y].append(x)
    pts.append((x, y))

c = 0 

for pt in pts:
    x, y = pt[0], pt[1]

    if max(mx[x]) > y > min(mx[x]) and max(my[y]) > x > min(my[y]): c += 1

print(c)

