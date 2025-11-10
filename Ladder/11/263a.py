import math

d = -1

for i in range(1, 6): 
    l = list(map(int, input().split()))
    
    if 1 in l:
        idx = l.index(1) + 1
        
        d = abs(3 - idx) + abs(3 - i)

print(d)
