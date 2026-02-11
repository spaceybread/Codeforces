for _ in range(int(input())):
    n = int(input())
    #n, x, y, z = (map(int, input().split()))
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    # s = input()
    
    if n % 9 != 0:
        print(0)
        continue
    
    c = 0
    for i in range(100):
        y = n + i
        ds = sum([int(l) for l in list(str(y))])
        if ds == i: c += 1
    
    print(c)

