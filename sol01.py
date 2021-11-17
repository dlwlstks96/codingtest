# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:56:54 2021

@author: s_dlwlstks96
"""    

#1463

n = int(input())

#결과값을 담기 위한 배열
#인덱스가 n값이라 생각하면 된다
dp = [0] * (n+1)

for i in range(2, n+1):
    #우선 dp[i] 값을 이전 값에서 +1을 해준다
    #왜냐하면 3 혹은 2로 안나누어질 경우
    #-1을 한 번 더 해주는게 이득이다
    dp[i] = dp[i-1] + 1 
    
    if i % 2 == 0:
        #위의 dp[i]값과 이전 i//2 값에 2를 곱한 값의 횟수 비교
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
        
print(dp[n])