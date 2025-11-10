n, m = map(int, input().split())
a = list(map(int, input().split()))

b = [[a[i], i + 1] for i in range(n)]

i = 0
while True:
    if len(b) == 1: 
        break
    
    p = b.pop(0)
    p[0] -= m

    if p[0] > 0: b.append(p)
    
    i += 1

    if i >= len(b): i = 0 

print(b[0][1])
