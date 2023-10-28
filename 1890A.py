for _ in range(int(input())):
    n = int(input())
    a = input().split()
    check = []
    
    for i in range(n):
        a[i] = int(a[i])
        
        if a[i] not in check:
            check.append(a[i])
    
    if len(check) > 2:
        print("No")
    elif len(check) == 1:
        print("Yes")
    else:
        con0 = a.count(check[0])
        con1 = a.count(check[1])
    
        if (abs(con0 - con1) < 2):
            print("Yes")
        else:
            print("No")
    
    
    
    
    
    
 
