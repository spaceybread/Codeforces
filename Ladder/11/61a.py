a = input()
b = input()

o = []

for i in range(len(a)):
    p, q = int(a[i]), int(b[i])
    o.append(str((p + q) % 2))

print("".join(o))
