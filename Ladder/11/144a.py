n = int(input())
a = list(map(int, input().split()))

mi, ma = min(a), max(a)
mi_id, ma_id = -1, -1

flag = True
for i in range(n):
    if a[i] == mi: mi_id = i
    
    if a[i] == ma and flag: 
        ma_id = i
        flag = False

t = (n - mi_id - 1) + (ma_id)

if mi_id < ma_id: t -= 1

print(t)

