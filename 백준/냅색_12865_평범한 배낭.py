# -*- coding: utf-8 -*-

# https://amber-chaeeunk.tistory.com/55

import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[0 for i in range(k+1)] for j in range(n+1)]

W = []
V = []

for _ in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
    
for i in range(1, n+1):
    for j in range(1, k+1):
        if j < W[i-1]: #현재 무게를 넣을 수 없다면
            dp[i][j] = dp[i-1][j]
        else: #현재 무게를 넣을 수 있다면 현재 무게 뺀 이전 값과 비교
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - W[i-1]] + V[i-1])
            
print(dp[n][k])

'''

#import itertools as it

n, k = map(int, input().split())

#dp = [0 for i in range(k+1)] #무게별 가치 정보

dp = [[i for i in range(n+1)] for i in range(k+1)]

data = [] #짐의 무게와 가치 정보

for i in range(n):
    w, v = map(int, input().split())
    
    if w > k: #버틸 수 없는 무게면 버리기
        continue
    
    data.append((w, v))
    
data.sort(key = lambda x: (x[0], -x[1]))

#tmp = sum(data[i][0] for i in range(2))
#print(tmp)
    
for i in range(k+1):
    for j in range(n+1):
        tmpWei = sum(data[_][0] for _ in range(j))
        if tmpWei > i:
            dp[i][j] = dp[i][j-1]
        else: #현재까지의 물건 무게가 가방 무게보다 같거나 클 때
            
        
#print(data)

#res = it.combinations(data, 2)
#for r in res:
#    print(r)

#for i in range(1, n+1):
#    res = it.combinations(data, i)
#    for r in res:
#        sumW = 0
#        sumV = 0
#        for j in r:
#            sumW += j[0]
#            sumV += j[1]
#            if sumW > k:
#                break
#        if sumW <= k:
#            dp[sumW] = max(dp[sumW], sumV)
        
print(max(dp))

'''