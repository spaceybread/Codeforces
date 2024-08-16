for _ in range(int(input())):
    n, k = (map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    
    ac, bc = 0, 0
    l, t = 0, 0
    for _ in range(n):
        o = a.pop(-1)
        if l == 0:
            ac += o
            l = 1
            t = o
        else:
            mn = min(t, o + k)
            diff = mn - o
            k -= diff
            bc += mn
            l = 0
    
    print(ac - bc)
    
