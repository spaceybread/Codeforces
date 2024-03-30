t = int(input())

for _ in range(t):
   n, k = map(int, input().split())

   if k == 1:
      out = []
      for i in range(n):
         out.append(str(i + 1))
      print(" ".join(out))
          
   elif k == n:
       print("1 " * n)
   else:
       print(-1)
