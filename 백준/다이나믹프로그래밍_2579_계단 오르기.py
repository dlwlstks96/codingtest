# -*- coding: utf-8 -*-

# n = 6
# data = [10, 20, 15, 25, 10, 20]

'''
10 20 20
10 15 10
20 25 20
'''

n = int(input())
data = [0]
for i in range(n):
    tmp = int(input())
    data.append(tmp)
    
if n <= 2:
    print(sum(data))
else:
    dp = [0] * (n+1)
    dp[1] = data[1]
    dp[2] = data[1] + data[2]
    
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i])
        
    print(dp[n])

# import sys

# n = int(input())
# data = [0]
# for i in range(n):
#     tmp = int(input())
#     data.append(tmp)
    
# if n == 1:
#     print(data[0])
#     sys.exit()
# elif n == 2:
#     print(data[0] + data[1])
#     sys.exit()

# step = [[] for i in range(n+1)] #계단을 밟는 과정을 저장할 리스트
# step_val = [0 for i in range(n+1)] #해당 계단까지의 최댓값을 저장할 리스트

# step[1].append(1) #0
# step_val[1] = data[1] #[10, 0 0 0 0 0]
# #step[1].append(0)
# #step[1].append(1) #0 1
# #step_val[1] = data[0] + data[1] #30

# for i in range(2, n+1):
#     if i-2 in step[i-1] and i-1 in step[i-1]: #연속 세개의 계단을 오를 과정이라면
#         step[i].append(i-2) #아래 아래 칸에서 지금 위치로 올라오기
#         step_val[i] = step_val[i-2] + data[i] #아래 아래 칸까지의 최댓값 + 내 값
#     else: #연속 세개의 계단을 오르는 과정을 고려하지 않아도 된다면    
#         tmp1 = data[i-2] #아래 아래 칸
#         tmp2 = data[i-1] #바로 아래 칸
#         if tmp1 >= tmp2:
#             step_val[i] = step_val[i-2] + data[i] #아래 아래 칸까지의 최댓값 + 내 값
#         else: #tmp < tmp2
#             step_val[i] = step_val[i-1] + data[i] #바로 아래 칸까지의 최댓값 + 내 값

# #print(step_val)
# print(step_val[-1]) #마지막 계단까지의 최댓값 출력
