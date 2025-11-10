n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

outa, outb = 0, 0

ma = {}
for i in range(n):
    ma[a[i]] = i

for x in b:
    outa += ma[x] + 1
    outb += (n - ma[x])

print(outa, outb)

