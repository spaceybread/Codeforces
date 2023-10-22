#isnt correct, runs presets 1-4 correctly but I have to check why it doesn't work for 5

for _ in range(int(input())):
    n = int(input())
    nums = input().split()
    for ins in range(n):
        nums[ins] = int(nums[ins])
    
    count = 0
    
    for i in range(n):
        j = i + 1
        while j < n:
            isValid = True
            for k in range(n):
                if (nums[i] % nums[k] == 0 and nums[j] % nums[k] == 0):
                    isValid = False
                    break
                
            if (isValid == True):
                count = count + 1
                
            j = j + 1
    
    print(count)
        
