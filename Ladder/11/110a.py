from collections import Counter as ct

s = str(input())
a = ct(s)

c = 0

if '4' in s: c += a['4']
if '7' in s: c += a['7']

if c == 7 or c == 4: 
    print('YES')
else: print('NO')
