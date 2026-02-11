for _ in range(int(input())):
#    n = int(input())
    p, q = (map(int, input().split()))
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    # s = input()
    
    if p < q and 2 * q <= 3 * p:
        print("Bob")
    else:
        print("Alice")

