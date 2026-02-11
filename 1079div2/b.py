for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    idx_map = {}
    for i in range(n): idx_map[a[i]] = i
    
    flag = True
    
    ds = []
    for x in b:
        if not ds or ds[-1] != x:
            ds.append(x)
        
    flag = True
    for i in range(len(ds) - 1):
        if idx_map[ds[i]] >= idx_map[ds[i+1]]:
            flag = False
            break


    if flag: print("YES")
    else: print("NO")
