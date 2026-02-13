from collections import Counter as ct
a = list(input())
b = list(input())
ab = a + b
abc = ct(ab)

c = ct(list(input()))

flag = True
for ch in c.keys(): flag = flag and (c[ch] <= abc[ch])

print("YES") if flag else print("NO")
