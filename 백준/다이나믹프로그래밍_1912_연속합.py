n = int(input())

if n == 1:
    l = int(input())
    print(l)
else:
    l = list(map(int, input().split()))
    
    dp = [0 for _ in range(n)]
    
    dp[0] = l[0]
    dp[1] = max(l[0]+l[1], l[1])
    
    # 10 / 10-4 / 10-4+3 / 10-4+3+1 
    # 10 / 6 / 9 / 10 / 15 / 21 / -14 / 12
    
    for i in range(2, n):
        dp[i] = max(dp[i-1] + l[i], l[i])
        
    print(max(dp))
