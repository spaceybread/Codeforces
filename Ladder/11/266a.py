n = int(input())
s = input()
f = [s[0]]

for i in range(1, n):
    if s[i] != f[-1]: f.append(s[i])

print(len(s) - len(f))
