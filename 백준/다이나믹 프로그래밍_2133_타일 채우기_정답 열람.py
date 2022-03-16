# -*- coding: utf-8 -*-

# https://ahn3330.tistory.com/81

n = int(input())

dp = [0 for i in range(31)]
dp[0] = 1

for i in range(2, n+1, 2):
    dp[i] = dp[i-2] * 3
    for j in range(0, i-2, 2):
        dp[i] += dp[j] * 2
        
print(dp[n])

'''
n = int(input())

if n % 2 != 0: #n이 홀수일 경우
    print(0)
else: #n이 짝수일 경우
    tmp = n // 2
    answer = (3**tmp) + (2*(tmp-1))
    print(answer)
''' 