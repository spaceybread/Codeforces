import math

ab, bc, ca = map(int, input().split())

b = ((ab * bc) // ca)**0.5
a = ((ab * ca) // bc)**0.5
c = ((ca * bc) // ab)**0.5


o = int(a + b + c) * 4
print(o)


