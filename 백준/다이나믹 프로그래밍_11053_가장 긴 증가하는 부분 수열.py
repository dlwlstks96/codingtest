# -*- coding: utf-8 -*-

# n = 9
# #data = [10, 20, 10, 30, 20, 50]
# data = [0, 10, 30, 20, 25, 40, 20, 30, 10, 50]

n = int(input())
data = [0] + list(map(int, input().split()))

dp = [0 for i in range(n+1)] #각 인덱스별 최댓값 담을 리스트


dp[1] = 1
for i in range(2, len(data)):
    # for j in range(len(data)):
    tmp = data[:i]
    prevMax = 0
    for j in range(len(tmp)):
        #현재 인덱스가 이전 dp 최댓값보다 크고 data가 나보다 작을 경우
        if tmp[j] < data[i] and dp[j] > prevMax:
            prevMax = dp[j] #최댓값 갱신
    dp[i] = prevMax+1 #dp테이블에서 내 최신값 갱신
    
print(max(dp))
        
        