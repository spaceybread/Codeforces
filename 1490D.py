def go(l, u, list, d):
    if len(list[l:u]) == 0:
        return
        
    m = max(list[l:u])
    mid = pos[m]
    
    dep[mid] = str(d)
    
    go(mid + 1, u, list, d + 1)
    go(l, mid, list, d + 1)


for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pos = {}

    dep = [-1] * n
    for i in range(n):
        pos[a[i]] = i

    go(0, n, a, 0)

    print(" ".join(dep))
