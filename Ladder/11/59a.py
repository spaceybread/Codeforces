s = input()

cs = "abcdefghijklmnopqrstuvwxyz"
c = 0

for x in s: 
    if x in cs: 
        c += 1

if c >= len(s) / 2: print(s.lower())
else: print(s.upper())



