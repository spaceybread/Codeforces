s = list(input())

out = []
i = 0

while i < len(s):
    if s[i] == '-':
        i += 1
        if s[i] == '-': out.append("2")
        else: out.append("1")
    else:
        out.append("0")
    i += 1

print("".join(out))


