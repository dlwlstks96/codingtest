n = int(input())

arr = [] #포도주 저장
dp = [0 for _ in range(n)]

for _ in range(n):
    tmp = int(input())
    arr.append(tmp)
    
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
elif n == 3:
    print(max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2]))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2])
    
    for i in range(3, n):
        dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2], dp[i-1])
        
    print(max(dp))
    
'''
6 10 13 9 8 1
6 / 16 / 23 / 28 / 

2156 포도주 시식

'''
