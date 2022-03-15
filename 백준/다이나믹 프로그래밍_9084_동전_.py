# -*- coding: utf-8 -*-

t = int(input())

for _ in range(t):
    n = int(input()) #동전의 가짓 수
    money = list(map(int, input().split()))
    goal = int(input())
    
    dp = [0 for d in range(goal+1)]
    
    dp[0] = 1 #초기값 1
    for i in range(n):
        for j in range(1, goal+1):
            if j >= money[i]:
                dp[j] += dp[j-money[i]]
            # 지금의 금액에서 money[i] 를 빼준다
            # 그 후 만들어야하는 금액이 지금 화폐 단위보다 크다면
            # 화폐 단위별로 건너뛰며 dp 테이블에 더해준다
                
    print(dp[goal])