n = int(input())
l, r = 0, 0

for i in range(n): 
    li, ri = map(int, input().split())
    l += li
    r += ri

s = 0

if 2 * l >= n: s +=  n - l
else: s += l

if 2 * r >= n: s +=  n - r
else: s += r

print(s)
