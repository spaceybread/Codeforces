p = [x for x in range(8, 50) if all([x % y != 0 for y in [2, 3, 5, 7]])]
p = sorted(p + [2, 3, 5, 7])

n, m = map(int, input().split())

id = p.index(n)

if id + 1 == len(p): 
    print("NO")
    exit()

if p[id + 1] == m: print("YES")
else: print("NO")
