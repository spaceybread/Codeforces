for _ in range(int(input())):
    l, r = (map(int, input().split()))
    L, R = (map(int, input().split()))
    
    c = 1
    for i in range(1, 101):
        if l <= i <= r and L <= i <= R:
            c+= 1
            
    if l == L:
        c -= 1
    if r == R:
        c -= 1
    
    print(c)
        
        
