s = int(input()) + 1

while True:
    t1 = s // 1000
    t2 = (s - t1 * 1000) // 100
    t3 = (s - t1 * 1000 - t2 * 100) // 10
    t4 = (s - t1 * 1000 - t2 * 100 - t3 * 10)
    
    b4 = [t4 == t3, t4 == t2, t4 == t1]
    b3 = [t3 == t2, t3 == t1]
    b2 = t2 == t1

    if any(b4): 
        t4 = (t4 + 1) % 10
        if t4 == 0: 
            t3 = (t3 + 1) % 10
            if t3 == 0:
                t2 = (t2 + 1) % 10
                if t2 == 0:
                    t1 += 1

    elif any(b3): 
        t3 = (t3 + 1) % 10
        t4 = 0
        if t3 == 0:
            t2 = (t2 + 1) % 10
            if t2 == 0:
                t1 += 1
    elif b2: 
        t2 = (t2 + 1) % 10
        t3 = 0
        t4 = 0
        if t2 == 0:
            t1 += 1

    else: break
    
    s = t1 * 1000 + t2 * 100 + t3 * 10 + t4

print(s)

