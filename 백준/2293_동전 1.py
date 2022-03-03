# -*- coding: utf-8 -*-

'''
dp 테이블
2, 3, 5원의 경우
  / 1 2 3 4 5 6 7 8 9 10 11 ..
  -----------------------------
2 / 0 1 0 1 0 1 0 1 0 1 0 .. 
3 / 0 0 1 0 1 1 1 1 2 1 2 ..
5 / 0 0 0 0 1 0 1 1 1 2 ..

'''

from sys import stdin

n, k = map(int, stdin.readline().split())

coins = []

for _ in range(n):
    coins.append(int(stdin.readline()))

count_list = [0] * (k + 1)
# x원짜리 동전 하나로 x원을 만드는 경우의 수 = 1
count_list[0] = 1

for i in coins:
    for j in range(i, k + 1):
        count_list[j] += count_list[j - i]

print(count_list[k])



'''아래가 내 풀이
import sys

n, k = 3, 10

# data = []
# for i in range(n):
#     data.append(int(input()))

data = [[2], [3], [5]]
res = [[2], [3], [5]]
min_data = [2 for i in range(100000//2)]

# answer = 0 
# for i in res:
#     for j in data:
#         if i+j == min_data:
#             sys.exit()
#         if i <= j and sum(i+j) <= 100000:
#             res.append(i+j)
#             if sum(i+j) == 1000:
#                 answer += 1
#             #print(sum(i+j))
        
print(2**31)
'''