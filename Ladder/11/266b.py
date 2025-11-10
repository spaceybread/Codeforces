n, t = map(int, input().split())
q = list(input())


for _ in range(t):
    
    i = 1
    while i < len(q):
        
        if q[i] == "G" and q[i - 1] == "B":
            q[i] = "B"
            q[i - 1] = "G"
            i += 2
        else: 
            i += 1

print("".join(q))


