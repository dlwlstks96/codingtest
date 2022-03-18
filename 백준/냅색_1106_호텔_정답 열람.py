# -*- coding: utf-8 -*-

INF = int(1e9)

c, n = map(int, input().split())

dp = [0] + [INF for i in range(c+100)] #0번 인덱스엔 0 넣는거 매우 중요

data = []

for i in range(n):
    pay, custom = map(int, input().split())
    data.append((pay, custom))

for cost, customer in data:
    for cur_customer in range(customer, c+100):
        #현재의 고객 수, [현재의 고객 수 - 도시 고객 수]의 비용 + 현재 도시의 비용
        dp[cur_customer] = min(dp[cur_customer], dp[cur_customer - customer] + cost)
        
print(min(dp[c:]))